import allure
from api_framework.base_api import BaseClient

class DeleteStudentByUuid(BaseClient):

    @allure.step("Delete student by id")
    def update_student(self, uuid):
        return self.put(f"/student/{uuid}")