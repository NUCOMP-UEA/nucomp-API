from typing import Optional

from pydantic import HttpUrl
from typing import Union
from site_project.domain.entities.base import BaseUser


class Coordinator(BaseUser):
    academic_title: str
    photo: Union[bytes, str]
    curriculum_lattes_url: Optional[str]
    linkedin_url: Optional[str]
    
    @classmethod
    def to_entity(cls, base_info, entity):
        base_info_dict = dict(base_info)
        user_dict = dict(entity)
        user_final_dict = {**base_info_dict, **user_dict}
        print(user_final_dict)
        del user_final_dict["_id"]
        return cls(**user_final_dict)
