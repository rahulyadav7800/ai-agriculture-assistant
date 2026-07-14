from backend.services.openrouter import openrouter_service


def main():

	result = openrouter_service.analyze_image(
		"backend/uploads/test.jpg"
	)

	print(result)


if __name__ == "__main__":

	main()
	