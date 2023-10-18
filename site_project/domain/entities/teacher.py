from typing import List, Optional
from uuid import UUID, uuid4

from pydantic.fields import Field
from pydantic import HttpUrl
from typing import Union
from site_project.domain.entities.base import BaseUser


class Teacher(BaseUser):
    related_subjects: List
    areas_of_interest: List
    academic_title: str
    personal_site: Optional[str]
    photo: Union[bytes, str]
    curriculum_lattes_url: Optional[str]
    linkedin_url: Optional[str]

    @classmethod
    def to_teacher(cls, base_info, teacher,file):
        base_info_dict = dict(base_info)
        teacher_dict = dict(teacher)
        teacher_final_dict = {**base_info_dict, **teacher_dict}
        teacher_final_dict['photo'] = file
        del teacher_final_dict["_id"]
        return cls(**teacher_final_dict)
