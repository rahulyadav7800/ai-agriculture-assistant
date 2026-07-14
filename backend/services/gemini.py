"""
File: gemini.py
Version: 2.1
Status: Stable
"""

import json
from pathlib import Path

from PIL import Image
from google import genai

from backend.config import settings
from backend.utils.logger import logger


SYSTEM_PROMPT = """
You are an expert plant pathologist and agricultural vision AI.

Analyze ONLY what is visible in the image.

Never guess hidden symptoms.

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
"""


class GeminiService:

	def __init__(self):

		self.client = genai.Client(
			api_key=settings.gemini_api_key
		)

		self.model = settings.gemini_vision_model

		logger.info(
			f"Gemini Vision Model : {self.model}"
		)

	def analyze_image(
		self,
		image_path: str
	) -> dict:

		image = Path(image_path)

		if not image.exists():

			raise FileNotFoundError(image_path)

		pil_image = Image.open(
			image_path
		)

		response = self.client.models.generate_content(

			model=self.model,

			contents=[
				pil_image,
				SYSTEM_PROMPT
			]

		)

		content = (
			response.text
			.replace("```json", "")
			.replace("```", "")
			.strip()
		)

		try:

			result = json.loads(
				content
			)

			confidence = result.get(
				"confidence",
				0
			)

			if isinstance(
				confidence,
				float
			) and confidence <= 1:

				result["confidence"] = round(
					confidence * 100,
					2
				)

			result["severity"] = result.get(
				"severity",
				"Unknown"
			).title()

			result["disease_stage"] = result.get(
				"disease_stage",
				"Unknown"
			).title()

			result["image_quality"] = result.get(
				"image_quality",
				"Unknown"
			).title()

			possible = result.get(
				"possible_disease",
				""
			)

			if isinstance(
				possible,
				str
			):

				if possible.lower() in [
					"none",
					"healthy",
					"no disease"
				]:

					result["possible_disease"] = ""

			return result

		except json.JSONDecodeError:

			logger.warning(
				"Gemini returned invalid JSON."
			)

			return {

				"is_healthy": False,

				"plant_part": "",

				"visible_symptoms": [],

				"possible_disease": "Unknown",

				"confidence": 0,

				"severity": "Unknown",

				"disease_stage": "Unknown",

				"affected_area_percent": 0,

				"reason": content,

				"recommendation": "",

				"image_quality": "Unknown",

				"needs_human_review": True

			}

	def health_check(
		self
	) -> bool:

		try:

			response = self.client.models.generate_content(

				model=self.model,

				contents="Reply only with OK."

			)

			return (
				response.text.strip().upper() == "OK"
			)

		except Exception as error:

			logger.exception(
				error
			)

			return False


gemini_service = GeminiService()