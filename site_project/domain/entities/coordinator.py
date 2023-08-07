from pydantic import BaseModel
from site_project.domain.entities.base import Base
from typing import Optional

class Coordinator(Base):
    academic_title : str
    photo: Optional[bytes]
    