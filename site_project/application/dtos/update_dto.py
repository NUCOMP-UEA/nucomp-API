from datetime import datetime

from pydantic import BaseModel


class UserUpdateDTO(BaseModel):
    name: str
    email: str
    gender: str
    course: str
    registration: str
    year_of_admission: datetime
    curriculum_lattes_url: str = None
    linkedin_url: str = None
