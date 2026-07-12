"""
File: test_openrouter.py
Version: 1.0
Status: Stable
"""

from backend.services.openrouter import openrouter_service


def main():

	print("=" * 60)
	print("Testing OpenRouter Service")
	print("=" * 60)

	print("\nChecking API Connection...\n")

	if not openrouter_service.health_check():

		print("❌ OpenRouter health check failed.")

		return

	print("✅ OpenRouter connection successful.\n")

	prompt = """
Plant Name:
Neem

Scientific Name:
Azadirachta indica

Please provide:

1. Short introduction
2. Common diseases
3. Organic treatment
4. Chemical treatment
5. Prevention tips

Keep the explanation beginner friendly.
"""

	print("Sending AI request...\n")

	response = openrouter_service.chat(prompt)

	print("=" * 60)
	print("AI Response")
	print("=" * 60)
	print(response)


if __name__ == "__main__":

	main()