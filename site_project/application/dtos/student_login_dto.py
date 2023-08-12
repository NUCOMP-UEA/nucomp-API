from pydantic import BaseModel

class StudentLoginDTO(BaseModel):
    username: str
    email:str
    password:str
