import allure
from api_framework.base_api import BaseClient

class GetStudentByUuid(BaseClient):

    @allure.step("Take student by id")
    def take_student(self, uuid):
        return self.get(f"/student/{uuid}")
