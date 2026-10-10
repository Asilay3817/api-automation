import pytest
from api_framework.students.students_api import StudentsClient
from api_framework.students.payloads import student_payload

@pytest.fixture
def students_client():
    return StudentsClient()

@pytest.fixture
def created_student(students_client):
    payload = student_payload()
    response = students_client.create(payload)
    assert response.status_code == 200, response.json()
    student = response.json()["student"]

    yield student
    students_client.delete_by_id(student["id"])