import pytest
import allure
from api_framework.models.student_model import StudentCreateUpdateModel
from api_framework.models.student_model import StudetUuidModel
from api_framework.models.student_model import StudentDeleteModel
from api_framework.models.student_model import AllStudentModel
from api_framework.students.payloads import student_payload

@allure.epic("Students system API")
@allure.feature("Management")
class TestStudents:


    @allure.story("Get All Students")
    @pytest.mark.regress
    def test_get_all_students(self, students_client):
        response = students_client.get_all()
        assert response.status_code == 200, response.json()

        model = AllStudentModel(**response.json())
        assert model.status == 1, response.json()


    @allure.story("Create Student")
    @pytest.mark.regress
    def test_create_student(self, students_client):
        payload = student_payload()
        response = students_client.create(payload)
        assert response.status_code == 200, response.json()
        model = StudentCreateUpdateModel(**response.json())
        students_client.helper.assert_student_matches(model.student, payload)

        student_id = model.student.id
        get_response = students_client.get_by_id(student_id)
        assert get_response.status_code == 200, get_response.json()
        model_get = StudetUuidModel(**get_response.json())
        students_client.helper.assert_student_matches(model_get.student, payload)

        delete_response = students_client.delete_by_id(student_id)
        assert delete_response.status_code == 200, delete_response.json()


    @allure.story("Create Student With Missing Fields")
    @pytest.mark.regress
    @pytest.mark.parametrize("field", [
        "email",
        "gender",
        "name",
        "phone_no",
        "status",
    ])


    def test_create_student_missing_fields(self, students_client, field):
        payload = student_payload()
        del payload[field]

        response = students_client.create(payload)
        assert response.status_code == 400, response.json()


    @allure.story("Update Student")
    @pytest.mark.regress
    def test_update_student(self, students_client, created_student):
        student_id = created_student["id"]
        new_payload = student_payload()
        response = students_client.update(student_id, new_payload)
        assert response.status_code == 200, response.json()

        model = StudentCreateUpdateModel(**response.json())
        students_client.helper.assert_student_matches(model.student, new_payload)

        get_response = students_client.get_by_id(student_id)
        assert get_response.status_code == 200, get_response.json()
        get_model = StudetUuidModel(**get_response.json())
        students_client.helper.assert_student_matches(get_model.student, new_payload)


    @allure.story("Update Student With Missing Fields")
    @pytest.mark.regress
    @pytest.mark.parametrize("field", [
        "email",
        "gender",
        "name",
        "phone_no",
        "status",
    ])


    def test_update_student_missing_fields(self, students_client, created_student, field):
        student_id = created_student["id"]
        payload = student_payload()
        del payload[field]

        response = students_client.update(student_id, payload)
        assert response.status_code == 400, response.json()


    @allure.story("Get student by invalid id")
    @pytest.mark.regress
    def test_get_student_invalid_id(self, students_client):
        response = students_client.get_by_id(9999999)
        assert response.status_code in (400, 404), response.json()


    @allure.story("Delete student")
    @pytest.mark.regress
    def test_delete_student(self, students_client):
        payload = student_payload()
        create_response = students_client.create(payload)
        assert create_response.status_code == 200, create_response.json()
        create_model = StudentCreateUpdateModel(**create_response.json())

        delete_response = students_client.delete_by_id(create_model.student.id)
        assert delete_response.status_code == 200
        model = StudentDeleteModel(**delete_response.json())
        assert model.status == 1, delete_response.json()

        get_response = students_client.get_by_id(create_model.student.id)
        assert get_response.status_code in (400, 404), get_response.json()