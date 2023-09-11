from datetime import datetime
from typing import List, Literal, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, HttpUrl
from pydantic.fields import Field


from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from pydantic.fields import Field
from uuid import UUID, uuid4


class NewsDTO(BaseModel):
    title: str
    caption: str
    image: Optional[bytes]
    published_at: datetime
    published_by: str
    tags: List

class BaseDTO(BaseModel):
    id_: UUID = Field(default_factory=uuid4)
    email: str
    gender: str
    course: str
    password: str
    user_type: Literal["student", "coordinator", "teacher"]


class StudentCreationDTO(BaseModel):
    name: str
    registration: str
    year_of_admission: datetime
    curriculum_lattes_url: str = None
    linkedin_url: str = None


class TeacherCreationDTO(BaseModel):
    name: str
    related_subjects: List
    areas_of_interest: List
    lattes_cv: HttpUrl
    academic_title: str
    personal_site: Optional[HttpUrl]
    photo: Optional[bytes]
    curriculum_lattes_url: str = None
    linkedin_url: str = None


class CoordinatorCreationDTO(BaseModel):
    name: str
    academic_title: str
    curriculum_lattes_url: str = None
    linkedin_url: str = None


class ArticleCreationDTO(BaseModel):
    authors: List[str]
    title: str
    published_in: str
    published_at: datetime
    article_url: str

class EventCreationDTO(BaseModel):
    title: str
    image: Optional[bytes]
    place: str
    date: datetime
    site_url: str

    