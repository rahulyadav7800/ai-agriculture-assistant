"""
File: scan_service.py
Version: 6.0
Status: Stable
"""

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
		query: str = "",
	) -> ScanResponse:

		logger.info(
			"Starting plant scan..."
		)

		image_path = image_service.save_image(
			file
		)

		logger.info(
			"Running PlantNet..."
		)

		plant = await plantnet_service.identify_plant(
			str(image_path)
		)

		logger.info(
			"Running Vision Model..."
		)

		vision = openrouter_service.analyze_image(
			str(image_path)
		)

		logger.info(
			"Running GPT..."
		)

		answer = openrouter_service.diagnose_plant(
			plant_result=plant,
			vision_result=vision,
			user_query=query
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