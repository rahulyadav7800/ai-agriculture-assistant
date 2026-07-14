from fastapi import APIRouter
from fastapi import HTTPException
from starlette import status

from backend.services.weather_service import weather_service
from backend.utils.logger import logger


router = APIRouter(
	prefix="/weather",
	tags=["Weather"]
)


@router.get(
	"/",
	summary="Get current weather"
)
async def get_weather(
	latitude: float,
	longitude: float
):

	try:

		return await weather_service.get_weather(
			latitude=latitude,
			longitude=longitude
		)

	except Exception as error:

		logger.exception(error)

		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail="Unable to fetch weather."
		)