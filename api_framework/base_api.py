import requests
from config import config

class BaseClient:
    def __init__(self) -> None:
        self.base_url = config.BASE_URL.rstrip("/")
        self.timeout = config.TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
        })
