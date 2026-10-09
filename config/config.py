import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL: str = os.getenv("BASE_URL", "")
    TIMEOUT: float = float(os.getenv("TIMEOUT", "15"))

conf = Config()