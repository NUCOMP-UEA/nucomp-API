from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel
from pydantic.fields import Field
from typing import Optional

class TypeUser(str, Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    COORDINATOR = "coordinator"


class BaseUser(BaseModel):
    id_: UUID = Field(default_factory=uuid4)
    name: Optional[str] = None
    email: str
    gender: str
    course: str
    password: str

    # @classmethod
    # def to_entity(cls, base_info, entity):
    #     base_info_dict = dict(base_info)
    #     user_dict = dict(entity)
    #     user_final_dict = {**base_info_dict, **user_dict}
    #     del user_final_dict["_id"]
    #     return cls(**user_final_dict)
