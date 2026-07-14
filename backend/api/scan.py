"""
File: scan.py
Version: 2.1
Status: Production Ready
"""

from fastapi import APIRouter
from fastapi import File
from fastapi import Form
from fastapi import HTTPException
from fastapi import UploadFile
from starlette import status

from backend.services.scan_service import scan_service
from backend.utils.logger import logger


router = APIRouter(
	prefix="/scan",
	tags=["Plant Scan"]
)


@router.post(
	"/",
	summary="Scan a plant image",
	description="""
Upload a plant image.

Pipeline:

1. PlantNet identifies the plant.
2. Vision AI detects visible symptoms.
3. Weather is fetched using user's location.
4. GPT answers the user's question using Vision, PlantNet and Weather.

The question is optional.
"""
)
async def scan_plant(
	file: UploadFile = File(...),
	query: str = Form(
		default="",
		description="""
Ask anything about this plant.

Examples:

- Which plant is this?
- Why are the leaves turning yellow?
- Which fertilizer should I use?
- How can I make this plant grow faster?
- Is this plant healthy?
"""
	),
):

	try:

		if file.content_type is None:

			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="Invalid file."
			)

		if not file.content_type.startswith("image/"):

			raise HTTPException(
				status_code=status.HTTP_400_BAD_REQUEST,
				detail="Only image files are allowed."
			)

		result = await scan_service.scan(
			file=file,
			query=query
		)

		return result

	except HTTPException:

		raise

	except Exception as error:

		logger.exception(error)

		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail=str(error)
		)