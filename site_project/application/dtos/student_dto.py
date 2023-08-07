from pydantic import BaseModel

class StudentDTO(BaseModel):
    name: str
    email:str
    gender: str
    course: str