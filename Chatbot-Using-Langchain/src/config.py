import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or ""
        self.OPENAI_MODEL = os.getenv("OPENAI_MODEL") or "gpt-3.5-turbo"
        self.TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE") or 0.3)

settings = Settings()
