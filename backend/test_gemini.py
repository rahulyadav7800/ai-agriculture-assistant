from backend.services.gemini import gemini_service

result = gemini_service.analyze_image(
	"backend/uploads/test.jpg"
)

print(result)