from datetime import datetime
from typing import Optional, List
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
    
    
class NewsUpdateDTO(BaseModel):
    title: Optional[str] = None
    caption: Optional[str] = None
    image: Optional[bytes] = None
    tags: Optional[List[str]] = None


class ArticleUpdateDTO(BaseModel):
    authors: Optional[List[str]] = None
    title: Optional[str] = None
    published_in: Optional[str] = None
    published_at: Optional[datetime] = None
    article_url: Optional[str] = None
    
class EventUpdateDTO(BaseModel):
    title: Optional[str] = None
    image: Optional[bytes] = None
    place: Optional[str] = None
    date: Optional[datetime] = None
    site_url: Optional[str] = None