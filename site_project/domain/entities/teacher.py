from pydantic import BaseModel
from site_project.domain.entities.base import Base
from typing import List, Optional

class Teacher(Base):
    related_subjects: List
    areas_of_interest: List
    personal_site: Optional[str]
    photo: Optional[bytes]
