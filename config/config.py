import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL: str = os.getenv("BASE_URL", "")
    TIMEOUT: float = float(os.getenv("TIMEOUT", "15"))

    def __post_init__(self):
        if not self.BASE_URL:
            raise ValueError("BASE_URL не задан")

config = Config()