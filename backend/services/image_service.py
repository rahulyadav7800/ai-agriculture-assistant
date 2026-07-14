"""
File: image_service.py
Version: 2.0
Status: Optimized
"""

import uuid
from pathlib import Path

from fastapi import UploadFile
from PIL import Image

from backend.utils.logger import logger
from backend.utils.paths import UPLOAD_DIR


class ImageService:

	ALLOWED_EXTENSIONS = {
		".jpg",
		".jpeg",
		".png",
		".webp"
	}

	MAX_SIZE = 1600

	JPEG_QUALITY = 85

	def validate_image(
		self,
		file: UploadFile
	):

		extension = Path(file.filename).suffix.lower()

		if extension not in self.ALLOWED_EXTENSIONS:

			logger.error(
				f"Unsupported image format: {extension}"
			)

			raise Exception(
				f"Unsupported image format: {extension}"
			)

	def compress_image(
		self,
		image_path: Path
	):

		image = Image.open(image_path)

		image.thumbnail(
			(self.MAX_SIZE, self.MAX_SIZE)
		)

		if image.mode in ("RGBA", "P"):

			image = image.convert("RGB")

		image.save(
			image_path,
			format="JPEG",
			quality=self.JPEG_QUALITY,
			optimize=True
		)

		size = image_path.stat().st_size / 1024

		logger.info(
			f"Compressed Image: {size:.2f} KB"
		)

	def save_image(
		self,
		file: UploadFile
	) -> Path:

		self.validate_image(file)

		filename = f"{uuid.uuid4()}.jpg"

		file_path = UPLOAD_DIR / filename

		with open(file_path, "wb") as image:

			image.write(
				file.file.read()
			)

		self.compress_image(
			file_path
		)

		logger.info(
			f"Image saved: {filename}"
		)

		return file_path


image_service = ImageService()