from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

BACKEND_DIR = PROJECT_ROOT / "backend"

DATABASE_DIR = BACKEND_DIR / "database"

UPLOAD_DIR = BACKEND_DIR / "uploads"

REPORT_DIR = BACKEND_DIR / "reports"

LOG_DIR = BACKEND_DIR / "logs"

MODEL_DIR = PROJECT_ROOT / "trained_models"

DATASET_DIR = PROJECT_ROOT / "datasets"


DATABASE_DIR.mkdir(parents=True, exist_ok=True)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)
MODEL_DIR.mkdir(parents=True, exist_ok=True)
DATASET_DIR.mkdir(parents=True, exist_ok=True)
