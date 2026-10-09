from api_framework.students.get_all_students import AllStudents
from api_framework.models.student_model import AllStudentModel
from api_framework.students.create_student import CreateStudent
from api_framework.models.student_model import StudentCreateUpdateModel

def test_get_student_list():
    students = AllStudents()
    response = students.students_list()
    assert response.status_code == 200, response.json()
    model = AllStudentModel(**response.json())

def test_create_student():
    student = CreateStudent()
    response = student.create_student()
    assert response.status_code == 200, response.json()
    model = StudentCreateUpdateModel(**response.json())