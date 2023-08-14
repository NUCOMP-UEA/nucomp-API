from datetime import datetime

from pydantic import BaseModel

from site_project.domain.entities.base import BaseUser


class Student(BaseUser):
    year_of_admission: datetime
    curriculum_lattes_url: str = None
    linkedin_url: str = None

    @classmethod
    def to_student(cls, base_info, student):
        base_info_dict = dict(base_info)
        student_dict = dict(student)
        student_final_dict = {**base_info_dict, **student_dict}
        del student_final_dict["_id"]
        return cls(**student_final_dict)
