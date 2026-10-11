import requests
import logging
from config.config import conf
from utils.helper import Helper

logger = logging.getLogger(__name__)

class BaseClient:
    def __init__(self) -> None:
        self.base_url = conf.BASE_URL.rstrip("/")
        self.timeout = conf.TIMEOUT
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
        self.helper = Helper()

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        kwargs.setdefault("timeout", self.timeout)
        logger.info("→ %s %s | body=%s", method, url, kwargs.get("json"))
        response = self.session.request(method, url, **kwargs)

        logger.info("← %s %s | status=%s | body=%s",method, url, response.status_code, response.text)

        self.helper.attach_response(response)
        return response


    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)