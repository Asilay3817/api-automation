from pydantic import BaseModel, field_validator

class StudentBaseModel(BaseModel):
    email: str | None = None
    gender: str
    id: int
    name: str
    phone_no: str
    status: int

    @field_validator("email", "gender", "id", "name", "phone_no", "status")
    def fields_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

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