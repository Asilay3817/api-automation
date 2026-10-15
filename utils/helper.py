import allure
from allure_commons.types import AttachmentType

class Helper:
    @staticmethod
    def attach_response(response, name: str = "API response"):
        allure.attach(
            body=response.text,
            name=name,
            attachment_type=AttachmentType.TEXT
        )

class Assertions:
    @staticmethod
    def assert_student_matches(student, payload: dict):
        assert student.name == payload["name"]
        assert student.email == payload["email"]
        assert student.gender == payload["gender"]
        assert student.phone_no == payload["phone_no"]
        assert student.status == payload["status"]