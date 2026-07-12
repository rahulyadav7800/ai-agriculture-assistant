from backend.services.openrouter import openrouter_service


def main():

	print("=" * 60)
	print("Testing OpenRouter Connection")
	print("=" * 60)

	if openrouter_service.health_check():
		print("✅ OpenRouter connection successful.\n")
	else:
		print("❌ OpenRouter connection failed.")
		return

	print("Sending test prompt...\n")

	response = openrouter_service.chat(
		"Hello! Reply with one sentence confirming that the AI Agriculture Assistant is working."
	)

	print("Response:\n")
	print(response)


if __name__ == "__main__":
	main()