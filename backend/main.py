from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.upload import router as upload_router
from backend.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):

	print(f"Starting {settings.app_name} v{settings.app_version}")

	yield

	print("Application stopped.")


app = FastAPI(
	title=settings.app_name,
	version=settings.app_version,
	debug=settings.debug,
	lifespan=lifespan
)


app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


# Register API Routers
app.include_router(upload_router)


@app.get("/", tags=["Home"])
async def home():

	return {
		"success": True,
		"application": settings.app_name,
		"version": settings.app_version,
		"message": "AI Agriculture Assistant Backend is running."
	}


@app.get("/health", tags=["Health"])
async def health():

	return {
		"status": "healthy",
		"debug": settings.debug,
		"model": settings.openrouter_model
	}