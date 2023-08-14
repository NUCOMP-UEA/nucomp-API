from abc import ABC, abstractmethod
from uuid import UUID

from site_project.application.dtos.creation_dto import StudentCreationDTO


class ICoordinator(ABC):
    @classmethod
    @abstractmethod
    def create(cls, student_dto: StudentCreationDTO):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_user(cls, email: str):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def update(cls, student_id: UUID, student):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def delete(cls, student):
        raise NotImplementedError
