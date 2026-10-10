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