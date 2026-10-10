import pytest
from api_framework.models.student_model import StudentCreateUpdateModel
from api_framework.students.payloads import student_payload


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
