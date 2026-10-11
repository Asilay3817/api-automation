import os
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL: str = os.getenv("BASE_URL", "http://93.77.188.34")
    TIMEOUT: float = float(os.getenv("TIMEOUT", "15"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE: str = os.getenv("LOG_FILE", "logs/test.log")

conf = Config()


def setup_logging() -> None:
    log_path = Path(conf.LOG_FILE)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=getattr(logging, conf.LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(),
        ],
        force=True,
    )