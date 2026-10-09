import allure
import json
from allure_commons.types import AttachmentType

class Helper:
    @staticmethod
    def attach_response(response, name: str = "API response"):
        allure.attach(
            body=json.dumps(response.json(), indent=4),
            name=name,
            attachment_type=AttachmentType.JSON
        )
