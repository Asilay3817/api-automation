import pytest
from api_framework.models.student_model import StudentCreateUpdateModel
from api_framework.models.student_model import StudetUuidModel
from api_framework.models.student_model import StudentDeleteModel
from api_framework.models.student_model import AllStudentModel
from api_framework.students.payloads import student_payload

def test_get_all_students(students_client):
    response = students_client.get_all()
    assert response.status_code == 200, response.json()

    model = AllStudentModel(**response.json())
    assert model.status == 1, response.json()

def test_create_student(students_client):
    payload = student_payload()
    response = students_client.create(payload)
    assert response.status_code == 200, response.json()
    model = StudentCreateUpdateModel(**response.json())
    assert model.student.name == payload["name"]
    assert model.student.email == payload["email"]
    assert model.student.gender == payload["gender"]
    assert model.student.phone_no == payload["phone_no"]
    assert model.student.status == payload["status"]

    student_id = model.student.id
    get_response = students_client.get_by_id(student_id)
    assert get_response.status_code == 200, get_response.json()
    model_get = StudetUuidModel(**get_response.json())
    assert model_get.student.name == payload["name"]
    assert model_get.student.email == payload["email"]
    assert model_get.student.gender == payload["gender"]
    assert model_get.student.phone_no == payload["phone_no"]
    assert model_get.student.status == payload["status"]

@pytest.mark.parametrize("field", [
    "email",
    "gender",
    "name",
    "phone_no",
    "status",
])

def test_create_student_missing_fields(students_client, field):
    payload = student_payload()
    del payload[field]

    response = students_client.create(payload)
    assert response.status_code == 400, response.json()

def test_update_student(students_client, created_student):
    student_id = created_student["id"]
    new_payload = student_payload()
    print("new_payload:", new_payload)
    response = students_client.update(student_id, new_payload)
    print("получил:", response.json())
    assert response.status_code == 200, response.json()

    model = StudentCreateUpdateModel(**response.json())
    assert model.student.name == new_payload["name"]
    assert model.student.email == new_payload["email"]
    assert model.student.gender == new_payload["gender"]
    assert model.student.phone_no == new_payload["phone_no"]
    assert model.student.status == new_payload["status"]

@pytest.mark.parametrize("field", [
    "email",
    "gender",
    "name",
    "phone_no",
    "status",
])

def test_update_student_missing_fields(students_client, created_student, field):
    student_id = created_student["id"]
    payload = student_payload()
    del payload[field]

    response = students_client.update(student_id, payload)
    assert response.status_code == 400, response.json()

def test_get_student_invalid_id(students_client):
    response = students_client.get_by_id(9999999)
    assert response.status_code in (400, 404), response.json()

def test_delete_student(students_client):
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



