import os
from dotenv import load_dotenv

load_dotenv()

# # Configuration-driven values
GEMINI_API_KEY = os.getenv("Gemini_class_1")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
HISTORY_LAST_N = int(os.getenv("HISTORY_LAST_N", "8"))