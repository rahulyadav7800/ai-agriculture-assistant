"""
File: scan_service.py
Version: 8.0
Status: Gemini Vision + OpenRouter Fallback
"""

import asyncio
import time

from fastapi import UploadFile

from backend.models.response import PlantResponse
from backend.models.response import ScanResponse
from backend.services.gemini import gemini_service
from backend.services.image_service import image_service
from backend.services.openrouter import openrouter_service
from backend.services.plantnet import plantnet_service
from backend.utils.logger import logger


class ScanService:

	def _analyze_vision(
		self,
		image_path: str
	) -> dict:

		try:

			logger.info(
				"Trying Gemini Vision..."
			)

			return gemini_service.analyze_image(
				image_path
			)

		except Exception as error:

			logger.warning(
				f"Gemini Vision failed: {error}"
			)

			logger.info(
				"Falling back to OpenRouter Vision..."
			)

			return openrouter_service.analyze_image(
				image_path
			)

	async def scan(
		self,
		file: UploadFile,
		query: str = ""
	) -> ScanResponse:

		logger.info(
			"Starting plant scan..."
		)

		image_path = image_service.save_image(
			file
		)

		logger.info(
			"Running PlantNet and Vision in parallel..."
		)

		start = time.perf_counter()

		plant_task = plantnet_service.identify_plant(
			str(image_path)
		)

		vision_task = asyncio.to_thread(
			self._analyze_vision,
			str(image_path)
		)

		plant, vision = await asyncio.gather(
			plant_task,
			vision_task
		)

		print(
			f"Plant + Vision Time: {time.perf_counter() - start:.2f}s"
		)

		logger.info(
			"Running GPT..."
		)

		start = time.perf_counter()

		answer = openrouter_service.diagnose_plant(
			plant_result=plant,
			vision_result=vision,
			user_query=query
		)

		print(
			f"GPT Time: {time.perf_counter() - start:.2f}s"
		)

		logger.info(
			"Plant scan completed successfully."
		)

		return ScanResponse(
			success=True,
			plant=PlantResponse(
				plant_name=plant["plant_name"],
				scientific_name=plant["scientific_name"],
				family=plant["family"],
				confidence=plant["confidence"]
			),
			diagnosis=answer
		)


scan_service = ScanService()