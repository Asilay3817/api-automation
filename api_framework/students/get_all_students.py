import allure

from api_framework.base_api import BaseClient

class AllStudents(BaseClient):

    @allure.step("Get students list")
    def students_list(self):
        return self.get("/student")