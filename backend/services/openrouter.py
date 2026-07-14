import json
import time

import httpx

from backend.config import settings
from backend.utils.image_encoder import image_encoder
from backend.utils.logger import logger
from backend.services.intent_detector import IntentDetector
from backend.services.prompt_builder import PromptBuilder


SYSTEM_PROMPT = """
You are an expert Agriculture AI Assistant.

Rules:

- Answer in the same language as the user.
- Never invent facts.
- If uncertain, clearly mention it.
- Prefer organic treatment first.
- Keep explanations practical.
- Return JSON only when requested.
"""


class OpenRouterService:

	def __init__(self):

		self.base_url = "https://openrouter.ai/api/v1/chat/completions"

		self.headers = {
			"Authorization": f"Bearer {settings.openrouter_api_key}",
			"Content-Type": "application/json",
			"HTTP-Referer": "http://localhost:8000",
			"X-Title": settings.app_name
		}

		self.timeout = httpx.Timeout(
			connect=30,
			write=180,
			read=180,
			pool=30
		)

		logger.info(
			f"Text Model : {settings.openrouter_text_model}"
		)

		logger.info(
			f"Vision Model : {settings.openrouter_vision_model}"
		)

	def _send_request(
		self,
		model: str,
		messages: list,
		temperature: float = 0.3,
		max_tokens: int = 1200
	) -> dict:

		payload = {
			"model": model,
			"messages": messages,
			"temperature": temperature,
			"max_tokens": max_tokens
		}

		response = httpx.post(
			self.base_url,
			headers=self.headers,
			json=payload,
			timeout=self.timeout
		)
		print("=" * 80)
		print(response.status_code)
		print(response.text)
		print("=" * 80)

		response.raise_for_status()

		return response.json()

	def _extract_content(
		self,
		data: dict
	) -> str:

		choices = data.get(
			"choices",
			[]
		)

		if not choices:

			raise Exception(
				"No response from OpenRouter."
			)

		content = (
			choices[0]
			.get("message", {})
			.get("content", "")
		)

		if not content:

			raise Exception(
				"Empty response."
			)

		return content.strip()

	def _vision_models(self) -> list[str]:

		models = [
			settings.openrouter_vision_model
		]

		if hasattr(
			settings,
			"openrouter_vision_fallback_model"
		):

			value = getattr(
				settings,
				"openrouter_vision_fallback_model"
			)

			if value:

				models.append(value)

		if hasattr(
			settings,
			"openrouter_vision_second_fallback"
		):

			value = getattr(
				settings,
				"openrouter_vision_second_fallback"
			)

			if value:

				models.append(value)

		return models

	def _vision_request(
		self,
		messages: list
	) -> dict:

		last_error = None

		for model in self._vision_models():

			try:

				logger.info(
					f"Trying Vision Model: {model}"
				)

				return self._send_request(
					model=model,
					messages=messages,
					temperature=0.1,
					max_tokens=800
				)

			except httpx.HTTPStatusError as error:

				last_error = error

				status = error.response.status_code

				if status == 429:

					logger.warning(
						f"{model} rate limited."
					)

					time.sleep(2)

					continue

				raise

			except Exception as error:

				last_error = error

				logger.exception(error)

				continue

		raise Exception(
			f"All vision models failed.\n{last_error}"
		)

	def chat(
		self,
		user_message: str
	) -> str:

		messages = [
			{
				"role": "system",
				"content": SYSTEM_PROMPT
			},
			{
				"role": "user",
				"content": user_message
			}
		]

		data = self._send_request(
			model=settings.openrouter_text_model,
			messages=messages
		)

		return self._extract_content(
			data
		)

	def diagnose_plant(
		self,
		plant_result: dict,
		vision_result: dict,
		user_query: str,
		weather: str = ""
	) -> str:

		intent_detector = IntentDetector()

		prompt_builder = PromptBuilder()

		intent = intent_detector.detect(
			user_query
		)

		prompt = prompt_builder.build(
			intent=intent,
			user_question=user_query,
			plantnet_result=json.dumps(
				plant_result,
				indent=2,
				ensure_ascii=False
			),
			vision_result=json.dumps(
				vision_result,
				indent=2,
				ensure_ascii=False
			)
		)

		response = self.chat(
			prompt
		)

		response = (
			response
			.replace("```json", "")
			.replace("```", "")
			.strip()
		)

		try:

			return json.loads(
				response
			)

		except json.JSONDecodeError:

			logger.warning(
				"GPT returned invalid JSON."
			)

			return {
				"type": "error",
				"message": response
			}

	def analyze_image(
		self,
		image_path: str
	) -> dict:

		image = image_encoder.encode_image(
			image_path
		)

		messages = [
			{
				"role": "user",
				"content": [
					{
						"type": "text",
"text": """
You are an expert plant pathologist and agricultural vision AI.

Analyze ONLY what is visible in the image.

Never guess hidden symptoms.

Never use external knowledge about the plant.

Never recommend treatment.

Return ONLY valid JSON.

{
	"is_healthy": true,
	"plant_part": "",
	"visible_symptoms": [],
	"possible_disease": "",
	"confidence": 0,
	"severity": "",
	"disease_stage": "",
	"affected_area_percent": 0,
	"reason": "",
	"recommendation": "",
	"image_quality": "",
	"needs_human_review": false
}

Rules:

1. Look only at the image.
2. Do not use markdown.
3. Do not explain outside JSON.
4. Confidence must be between 0 and 100.
5. If confidence is below 50:
	- possible_disease = "Unknown"
	- needs_human_review = true
6. Severity must be one of:
	"None"
	"Low"
	"Medium"
	"High"
7. Disease stage must be one of:
	"Healthy"
	"Early"
	"Moderate"
	"Advanced"
	"Unknown"
8. recommendation should contain one short sentence describing what should be inspected next.
9. affected_area_percent must be an integer.
10. visible_symptoms must contain only symptoms that are actually visible.
11. Return JSON only.
"""	
					},
					{
						"type": "image_url",
						"image_url": {
							"url": image
						}
					}
				]
			}
		]

		data = self._vision_request(
			messages
		)

		content = self._extract_content(
			data
		)

		content = (
			content
			.replace("```json", "")
			.replace("```", "")
			.strip()
		)

		try:

			return json.loads(
				content
			)

		except json.JSONDecodeError:

			logger.warning(
				"Vision model returned invalid JSON."
			)

			return {
				"is_healthy": False,
				"plant_part": "",
				"visible_symptoms": [],
				"possible_disease": "Unknown",
				"confidence": 0,
				"severity": "Unknown",
				"reason": content,
				"image_quality": "Unknown"
			}

	def health_check(
		self
	) -> bool:

		try:

			reply = self.chat(
				"Reply only with OK."
			)

			return (
				reply.strip().upper() == "OK"
			)

		except Exception as error:

			logger.exception(
				f"Health Check Failed: {error}"
			)

			return False

	def close(
		self
	):

		logger.info(
			"OpenRouter service closed."
		)


openrouter_service = OpenRouterService()