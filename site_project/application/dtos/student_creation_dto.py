from pydantic import BaseModel


class StudentCreationDTO(BaseModel):
    name: str
    email: str
    gender: str
    course: str
    password: str
    username: str


class StudentLoginDTO(BaseModel):
    email: str
    password: str
