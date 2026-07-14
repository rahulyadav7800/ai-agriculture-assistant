"""
File: image_encoder.py
Version: 2.0
Status: Production Ready
"""

import base64
import io
from pathlib import Path

from PIL import Image, ImageOps


class ImageEncoder:

	_MIME_TYPES = {
		".jpg": "image/jpeg",
		".jpeg": "image/jpeg",
		".png": "image/png",
		".webp": "image/webp"
	}

	MAX_SIZE = (1024, 1024)
	JPEG_QUALITY = 85

	def encode_image(
		self,
		image_path: str | Path
	) -> str:

		image_path = Path(image_path)

		if not image_path.exists():

			raise FileNotFoundError(
				f"Image not found: {image_path}"
			)

		extension = image_path.suffix.lower()

		if extension not in self._MIME_TYPES:

			raise ValueError(
				f"Unsupported image format: {extension}"
			)

		with Image.open(image_path) as image:

			image = ImageOps.exif_transpose(image)

			if image.mode != "RGB":

				image = image.convert("RGB")

			image.thumbnail(
				self.MAX_SIZE,
				Image.Resampling.LANCZOS
			)

			buffer = io.BytesIO()

			image.save(
				buffer,
				format="JPEG",
				quality=self.JPEG_QUALITY,
				optimize=True
			)

			image_bytes = buffer.getvalue()

		image_base64 = base64.b64encode(
			image_bytes
		).decode("utf-8")

		return (
			f"data:image/jpeg;base64,"
			f"{image_base64}"
		)


image_encoder = ImageEncoder()