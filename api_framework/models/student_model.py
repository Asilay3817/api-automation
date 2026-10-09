from pydantic import BaseModel, field_validator

class StudentBaseModel(BaseModel):
    email: str | None = None
    gender: str
    id: int
    name: str
    phone_no: str
    status: int

class AllStudentModel(BaseModel):
    status: int
    students: list[StudentBaseModel]

class StudetUuidModel(BaseModel):
    status: int
    student: StudentBaseModel

class StudentCreateUpdateModel(BaseModel):
    message: str
    status: int
    student: StudentBaseModel

class StudentDeleteModel(BaseModel):
    message: str
    status: int