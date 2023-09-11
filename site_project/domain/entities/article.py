from pydantic import BaseModel
from typing import List
from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel
from pydantic.fields import Field


class Article(BaseModel):
    id_: UUID = Field(default_factory=uuid4)
    authors: List[str]
    title: str
    published_in: str
    published_at: datetime
    article_url: str
