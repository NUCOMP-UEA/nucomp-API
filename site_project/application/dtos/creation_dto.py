from pydantic import BaseModel


class BaseDTO(BaseModel):
    name: str
    email:str
    gender: str
    course: str
    username:str
    password:str

class StudentCreationDTO(BaseDTO):
    pass

class TeacherDTO(BaseDTO):
    pass
