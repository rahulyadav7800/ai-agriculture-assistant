"""
File: plantnet.py
Version: 1.0
Status: Stable
"""

import mimetypes
from pathlib import Path

import httpx

from backend.config import settings
from backend.utils.logger import logger


class PlantNetService:

	def __init__(self):

		self.base_url = "https://my-api.plantnet.org/v2/identify/all"

		self.timeout = 60

		logger.info("PlantNet service initialized.")

	async def identify_plant(
		self,
		image_path: str,
		organ: str = "leaf"
	) -> dict:

		image = Path(image_path)

		if not image.exists():

			logger.error(f"Image not found: {image}")

			raise FileNotFoundError(f"Image not found: {image}")

		mime_type = mimetypes.guess_type(image.name)[0]

		if mime_type is None:
			mime_type = "application/octet-stream"

		url = (
			f"{self.base_url}"
			f"?api-key={settings.plantnet_api_key}"
		)

		try:

			with image.open("rb") as file:

				files = {
					"images": (
						image.name,
						file,
						mime_type
					)
				}

				data = {
					"organs": organ
				}

				async with httpx.AsyncClient(
					timeout=self.timeout
				) as client:

					response = await client.post(
						url,
						files=files,
						data=data
					)

			response.raise_for_status()

			result = response.json()

			logger.info("Plant identification successful.")

			return self._parse_result(result)

		except httpx.TimeoutException:

			logger.exception("PlantNet request timed out.")

			raise Exception(
				"PlantNet request timed out."
			)

		except httpx.HTTPStatusError as error:

			logger.exception(
				f"PlantNet HTTP Error: {error.response.status_code}"
			)

			raise Exception(error.response.text)

		except Exception as error:

			logger.exception(
				f"Unexpected PlantNet Error: {error}"
			)

			raise

	def _parse_result(
		self,
		result: dict
	) -> dict:

		results = result.get("results", [])

		if not results:

			logger.warning("No plant identified.")

			raise Exception("No plant identified.")

		best_match = results[0]

		species = best_match.get("species", {})

		common_names = species.get(
			"commonNames",
			[]
		)

		family = species.get(
			"family",
			{}
		)

		return {

			"plant_name": (
				common_names[0]
				if common_names
				else "Unknown"
			),

			"scientific_name": species.get(
				"scientificNameWithoutAuthor",
				"Unknown"
			),

			"family": family.get(
				"scientificName",
				"Unknown"
			),

			"confidence": round(
				best_match.get("score", 0) * 100,
				2
			),

			"raw_response": result
		}

	def health_check(self) -> bool:

		return bool(settings.plantnet_api_key)


plantnet_service = PlantNetService()