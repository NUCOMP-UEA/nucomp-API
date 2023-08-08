from pydantic import BaseModel

class StudentLoginDTO(BaseModel):
    name: str
    email:str
    password:str