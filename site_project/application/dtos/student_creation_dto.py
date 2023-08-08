from pydantic import BaseModel

class StudentCreationDTO(BaseModel):
    name: str
    email:str
    gender: str
    course: str