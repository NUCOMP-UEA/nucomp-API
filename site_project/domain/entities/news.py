from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from pydantic.fields import Field
from uuid import UUID, uuid4


class News(BaseModel):
    id_: UUID = Field(default_factory=uuid4)
    title: str
    caption: str
    image: Optional[bytes]
    published_at: datetime
    published_by: str
    tags: List
