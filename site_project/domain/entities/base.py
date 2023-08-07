from pydantic import BaseModel

class Base(BaseModel):
    name: str
    email:str
    gender: str
    course: str
    curriculum_lattes_url: str
    linkedin_url: str