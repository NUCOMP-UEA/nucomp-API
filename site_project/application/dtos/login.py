from pydantic import BaseModel


class Base(BaseModel):
    email: str
    password: str


class StudentLoginDTO(Base):
    pass


class TeacherLoginDTO(Base):
    pass
