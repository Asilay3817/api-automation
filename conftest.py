import pytest
import allure
from pathlib import Path
from allure_commons.types import AttachmentType
from config.config import setup_logging
from api_framework.students.students_api import StudentsClient
from api_framework.students.payloads import student_payload

setup_logging()

@pytest.fixture(autouse=True)
def attach_log_to_allure():
    log_file = Path("logs/test.log")
    log_file.write_text("")

    yield

    if log_file.exists():
        log_content = log_file.read_text(encoding="utf-8")
        allure.attach(
            body=log_content,
            name="test.log",
            attachment_type=AttachmentType.TEXT,
        )

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