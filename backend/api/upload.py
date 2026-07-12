"""
File: upload.py
Version: 1.0
Status: Stable
"""

from fastapi import APIRouter
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile

from backend.services.image_service import image_service
from backend.services.plantnet import plantnet_service
from backend.services.openrouter import openrouter_service
from backend.utils.logger import logger


router = APIRouter(
	prefix="/upload",
	tags=["Upload"]
)


@router.post("/")
async def upload_image(
	file: UploadFile = File(...)
):

	try:

		image_path = image_service.save_image(file)

		plant = await plantnet_service.identify_plant(
			str(image_path)
		)

		diagnosis = openrouter_service.diagnose_plant(
			plant_name=plant["plant_name"],
			symptoms="No symptoms provided."
		)

		return {
			"success": True,
			"plant": plant,
			"diagnosis": diagnosis
		}

	except Exception as error:

		logger.exception(error)

		raise HTTPException(
			status_code=500,
			detail=str(error)
		)
	