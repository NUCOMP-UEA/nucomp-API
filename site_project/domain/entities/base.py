from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel
from pydantic.fields import Field


class TypeUser(str, Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    COORDINATOR = "coordinator"


class BaseUser(BaseModel):
    id_: UUID
    name: str
    email: str
    gender: str
    course: str
    password: str

    @classmethod
    def to_entity(cls, base_info, student):
        base_info_dict = dict(base_info)
        student_dict = dict(student)
        student_final_dict = {**base_info_dict, **student_dict}
        del student_final_dict["_id"]
        return cls(**student_final_dict)
