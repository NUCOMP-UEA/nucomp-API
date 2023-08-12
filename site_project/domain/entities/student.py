from pydantic import BaseModel
from datetime import datetime
from site_project.domain.entities.base import Base


class Student(Base):
    registration: str
    year_of_admission: datetime
    
    @classmethod
    def to_student(cls):
        pass
    
    
    