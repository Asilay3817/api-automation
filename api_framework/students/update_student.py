import allure
from api_framework.base_api import BaseClient

class UpdateStudentByUuid(BaseClient):

    @allure.step("Update student by id")
    def update_student(self, uuid):
        return self.put(f"/student/{uuid}")