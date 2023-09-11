from abc import ABC, abstractmethod
from uuid import UUID

from site_project.application.dtos.creation_dto import TeacherCreationDTO


class ITeacherRepository(ABC):
    @classmethod
    @abstractmethod
    async def create(cls, teacher: TeacherCreationDTO):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    async def get_user(cls, teacher_id: UUID):
        return NotImplementedError

    @classmethod
    @abstractmethod
    async def update(cls, teacher_id: UUID, teacher):
        return NotImplementedError

    @classmethod
    @abstractmethod
    async def delete(cls, teacher_id):
        return NotImplementedError
