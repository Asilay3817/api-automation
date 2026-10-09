import allure
from api_framework.base_api import BaseClient
from api_framework.students.payloads import Payloads

class CreateStudent(BaseClient):

    @allure.step("Create student")
    def create_student(self):
        return self.post("/student", json=Payloads.create_student)