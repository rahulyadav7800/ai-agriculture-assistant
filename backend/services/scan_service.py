"""
File: scan_service.py
Version: 7.0
Status: Optimized
"""

import asyncio
import time

from fastapi import UploadFile

from backend.models.response import PlantResponse
from backend.models.response import ScanResponse
from backend.services.image_service import image_service
from backend.services.openrouter import openrouter_service
from backend.services.plantnet import plantnet_service
from backend.utils.logger import logger


class ScanService:

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
			openrouter_service.analyze_image,
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