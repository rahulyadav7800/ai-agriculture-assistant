"""
File: test_plantnet.py
Version: 1.0
Status: Stable
"""

import asyncio
from pathlib import Path

from backend.services.plantnet import plantnet_service


async def main():

	image_path = Path("backend/uploads/test.jpg")

	if not image_path.exists():

		print("Test image not found.")
		return

	result = await plantnet_service.identify_plant(
		str(image_path)
	)

	print("\nPlantNet Result\n")

	for key, value in result.items():

		if key == "raw_response":
			continue

		print(f"{key}: {value}")


if __name__ == "__main__":

	asyncio.run(main())