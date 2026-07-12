import httpx

from backend.config import settings
from backend.utils.logger import logger


SYSTEM_PROMPT = """
You are an expert Agriculture AI Assistant.

Rules:

- Answer in the same language as the user.
- Never invent facts.
- If you are uncertain, clearly mention that the diagnosis is only a possibility.
- Prefer organic treatment before chemical treatment.
- Keep explanations practical and beginner friendly.
- Give step-by-step recommendations whenever possible.
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

		self.timeout = 60

		logger.info(
			f"OpenRouter initialized with model: {settings.openrouter_model}"
		)

	def _send_request(self, messages: list) -> dict:

		payload = {
			"model": settings.openrouter_model,
			"messages": messages,
			"temperature": 0.3,
			"max_tokens": 1200
		}

		try:

			response = httpx.post(
				self.base_url,
				headers=self.headers,
				json=payload,
				timeout=self.timeout
			)

			response.raise_for_status()

			data = response.json()

			logger.info("OpenRouter request completed successfully.")

			return data

		except httpx.TimeoutException:

			logger.exception("OpenRouter request timed out.")

			raise Exception(
				"OpenRouter request timed out."
			)

		except httpx.HTTPStatusError as error:

			logger.exception(
				f"HTTP Error {error.response.status_code}: {error.response.text}"
			)

			raise Exception(
				f"HTTP Error: {error.response.status_code}"
			)

		except Exception as error:

			logger.exception(
				f"Unexpected OpenRouter Error: {error}"
			)

			raise

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

		data = self._send_request(messages)

		choices = data.get("choices", [])

		if not choices:

			logger.error(
				"OpenRouter returned no choices."
			)

			raise Exception(
				"No response received from OpenRouter."
			)

		message = choices[0].get("message", {})

		content = message.get("content")

		if not content:

			logger.error(
				"OpenRouter returned an empty message."
			)

			raise Exception(
				"OpenRouter returned an empty message."
			)

		return content.strip()

	def diagnose_plant(
		self,
		plant_name: str,
		symptoms: str,
		weather: str = ""
	) -> str:

		prompt = f"""
Plant Name:
{plant_name}

Symptoms:
{symptoms}

Weather:
{weather}

Analyze the plant and provide:

1. Possible Disease
2. Confidence (Approximate)
3. Reason
4. Organic Treatment
5. Chemical Treatment
6. Prevention
7. Recovery Time
8. Additional Advice
"""

		return self.chat(prompt)

	def analyze_symptoms(
		self,
		symptoms: str
	) -> str:

		prompt = f"""
Symptoms:

{symptoms}

Analyze these symptoms and provide:

1. Possible Disease
2. Confidence
3. Reason
4. Organic Treatment
5. Chemical Treatment
6. Prevention
"""

		return self.chat(prompt)

	def health_check(self) -> bool:

		try:

			reply = self.chat(
				"Reply only with the word OK."
			)

			return "OK" in reply.upper()

		except Exception as error:

			logger.exception(
				f"Health Check Failed: {error}"
			)

			return False

	def close(self):

		logger.info(
			"OpenRouter service closed."
		)


openrouter_service = OpenRouterService()