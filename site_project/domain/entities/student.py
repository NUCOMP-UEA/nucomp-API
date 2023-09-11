from datetime import datetime
from typing import Optional

from pydantic import HttpUrl

from site_project.domain.entities.base import BaseUser


class Student(BaseUser):
    year_of_admission: datetime
    curriculum_lattes_url: Optional[str]
    linkedin_url: Optional[str]

    @classmethod
    def to_student(cls, base_info, student):
        base_info_dict = dict(base_info)
        student_dict = dict(student)
        student_final_dict = {**base_info_dict, **student_dict}
        del student_final_dict["_id"]
        return cls(**student_final_dict)
