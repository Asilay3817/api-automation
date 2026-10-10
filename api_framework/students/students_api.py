import allure
from api_framework.base_api import BaseClient

class StudentsClient(BaseClient):

    @allure.step("Create student")
    def create(self, payload: dict):
        return self.post("/student", json=payload)

    @allure.step("Get students list")
    def get_all(self):
        return self.get("/student")

    @allure.step("Take student by id")
    def get_by_id(self, id):
        return self.get(f"/student/{id}")

    @allure.step("Update student by id")
    def update(self, id, payload: dict):
        return self.put(f"/student/{id}", json=payload)

    @allure.step("Delete student by id")
    def delete_by_id(self, id):
        return self.delete(f"/student/{id}")