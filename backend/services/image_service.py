"""
File: image_service.py
Version: 1.0
Status: Stable
"""

import uuid
from pathlib import Path

from fastapi import UploadFile

from backend.config import settings
from backend.utils.logger import logger
from backend.utils.paths import UPLOAD_DIR


class ImageService:

	ALLOWED_EXTENSIONS = {
		".jpg",
		".jpeg",
		".png",
		".webp"
	}

	def validate_image(
		self,
		file: UploadFile
	):

		extension = Path(file.filename).suffix.lower()

		if extension not in self.ALLOWED_EXTENSIONS:

			logger.error(f"Unsupported image format: {extension}")

			raise Exception(
				f"Unsupported image format: {extension}"
			)

	def save_image(
		self,
		file: UploadFile
	) -> Path:

		self.validate_image(file)

		extension = Path(file.filename).suffix.lower()

		filename = f"{uuid.uuid4()}{extension}"

		file_path = UPLOAD_DIR / filename

		with open(file_path, "wb") as image:

			image.write(file.file.read())

		logger.info(f"Image saved: {filename}")

		return file_path


image_service = ImageService()
