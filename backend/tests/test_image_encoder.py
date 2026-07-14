from pathlib import Path

from backend.utils.image_encoder import image_encoder


def main():

	image_path = "backend/uploads/test.jpg"

	before = Path(image_path).stat().st_size / 1024

	print(f"Original : {before:.2f} KB")

	data = image_encoder.encode_image(
		image_path
	)

	print(data[:100])

	print(
		f"Base64 Length : {len(data):,}"
	)


if __name__ == "__main__":

	main()