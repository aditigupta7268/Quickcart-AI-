import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env from the backend/ directory, no matter where the process is started from
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=_env_path)

DATABASE_URL = os.getenv("DATABASE_URL")

REDIS_HOST = os.getenv("REDIS_HOST")

REDIS_PORT = os.getenv("REDIS_PORT")

RAZORPAY_KEY = os.getenv("RAZORPAY_KEY")

RAZORPAY_SECRET = os.getenv("RAZORPAY_SECRET")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")