from typing import List, Optional
from uuid import UUID, uuid4

from pydantic.fields import Field
from pydantic import HttpUrl

from site_project.domain.entities.base import BaseUser


class Teacher(BaseUser):
    related_subjects: List
    areas_of_interest: List
    academic_title: str
    personal_site: Optional[str]
    photo: Optional[bytes]
    curriculum_lattes_url: Optional[str]
    linkedin_url: Optional[str]

    @classmethod
    def to_teacher(cls, base_info, student):
        base_info_dict = dict(base_info)
        student_dict = dict(student)
        student_final_dict = {**base_info_dict, **student_dict}
        del student_final_dict["_id"]
        return cls(**student_final_dict)
