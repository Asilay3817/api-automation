import allure
import json
from allure_commons.types import AttachmentType

class Helper:
    def attch_response(self, response):
        response=json.dump(response, indent=4)
        allure.attach(body=response,name="API response", attachment_type=AttachmentType.JSON)
