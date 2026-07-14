from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	model_config = SettingsConfigDict(
		env_file=".env",
		env_file_encoding="utf-8",
		case_sensitive=True,
		extra="ignore"
	)

	# ==========================================
	# Application
	# ==========================================

	app_name: str = Field(default="AI Agriculture Assistant", alias="APP_NAME")
	app_version: str = Field(default="1.0.0", alias="APP_VERSION")
	debug: bool = Field(default=True, alias="DEBUG")

	# ==========================================
	# Server
	# ==========================================

	host: str = Field(default="127.0.0.1", alias="HOST")
	port: int = Field(default=8000, alias="PORT")

	# ==========================================
	# Database
	# ==========================================

	database_url: str = Field(
		default="sqlite:///database/agriculture.db",
		alias="DATABASE_URL"
	)

	# ==========================================
	# OpenRouter
	# ==========================================

	openrouter_api_key: str = Field(
		default="",
		alias="OPENROUTER_API_KEY"
	)

	openrouter_text_model: str = Field(
		default="openai/gpt-oss-120b:free",
		alias="OPENROUTER_TEXT_MODEL"
	)

	openrouter_vision_model: str = Field(
		default="google/gemma-4-31b-it:free",
		alias="OPENROUTER_VISION_MODEL"
	)

	openrouter_vision_fallback_model: str = Field(
		default="google/gemma-4-26b-a4b-it:free",
		alias="OPENROUTER_VISION_FALLBACK_MODEL"
	)

	openrouter_vision_second_fallback: str = Field(
		default="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
		alias="OPENROUTER_VISION_SECOND_FALLBACK"
	)

		# ==========================================
	# Gemini
	# ==========================================

	gemini_api_key: str = Field(
		default="",
		alias="GEMINI_API_KEY"
	)

	gemini_vision_model: str = Field(
		default="gemini-2.5-flash",
		alias="GEMINI_VISION_MODEL"
	)


		# ==========================================
	# PlantNet
	# ==========================================

	plantnet_api_key: str = Field(
		default="",
		alias="PLANTNET_API_KEY"
	)
	# ==========================================
	# Weather
	# ==========================================

	openweather_api_key: str = Field(default="", alias="OPENWEATHER_API_KEY")

	# ==========================================
	# AssemblyAI
	# ==========================================

	assemblyai_api_key: str = Field(default="", alias="ASSEMBLYAI_API_KEY")

	# ==========================================
	# Uploads
	# ==========================================

	upload_folder: str = Field(
		default="backend/uploads",
		alias="UPLOAD_FOLDER"
	)

	max_image_size_mb: int = Field(
		default=10,
		alias="MAX_IMAGE_SIZE_MB"
	)

	# ==========================================
	# AI
	# ==========================================

	yolo_model: str = Field(
		default="trained_models/plant_disease.pt",
		alias="YOLO_MODEL"
	)

	confidence_threshold: float = Field(
		default=0.50,
		alias="CONFIDENCE_THRESHOLD"
	)

	# ==========================================
	# Logging
	# ==========================================

	log_level: str = Field(default="INFO", alias="LOG_LEVEL")

	# ==========================================
	# Security
	# ==========================================

	secret_key: str = Field(default="", alias="SECRET_KEY")
	jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")

	access_token_expire_minutes: int = Field(
		default=60,
		alias="ACCESS_TOKEN_EXPIRE_MINUTES"
	)


@lru_cache
def get_settings() -> Settings:
	return Settings()


settings = get_settings()