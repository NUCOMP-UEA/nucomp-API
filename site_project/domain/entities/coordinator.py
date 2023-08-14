from typing import Optional

from pydantic import HttpUrl

from site_project.domain.entities.base import BaseUser


class Coordinator(BaseUser):
    academic_title: str
    photo: Optional[bytes]
    curriculum_lattes_url: Optional[str]
    linkedin_url: Optional[str]
