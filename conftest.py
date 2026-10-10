import pytest
from api_framework.students.students_api import StudentsClient

@pytest.fixture
def students_client():
    return StudentsClient()