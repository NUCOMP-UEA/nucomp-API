from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from pydantic.fields import Field
from uuid import UUID, uuid4


class Event(BaseModel):
    id_: UUID = Field(default_factory=uuid4)
    title: str
    image: Optional[bytes]
    place: str
    date: datetime
    site_url: str
