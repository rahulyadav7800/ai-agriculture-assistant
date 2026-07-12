from pathlib import Path
import sys

from loguru import logger

from backend.config import settings


log_directory = Path("backend/logs")
log_directory.mkdir(parents=True, exist_ok=True)

log_file = log_directory / "application.log"

logger.remove()

logger.add(
	sys.stdout,
	level=settings.log_level,
	colorize=True,
	format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level:<8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>"
)

logger.add(
	log_file,
	level=settings.log_level,
	rotation="10 MB",
	retention="30 days",
	compression="zip",
	enqueue=True,
	format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {name}:{function}:{line} | {message}"
)