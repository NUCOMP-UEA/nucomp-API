from pydantic import BaseModel

class Base(BaseModel):
    name: str
    email:str
    gender: str
    course: str 
    password:str
    curriculum_lattes_url: str = None
    linkedin_url: str = None
    