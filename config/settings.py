# config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SERPAPI_KEY = os.getenv("SERPAPI_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GOOGLE_SHEETS_API_KEY = os.getenv("GOOGLE_SHEETS_API_KEY")