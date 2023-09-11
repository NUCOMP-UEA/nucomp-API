from abc import ABC, abstractmethod
from uuid import UUID

from site_project.application.dtos.creation_dto import CoordinatorCreationDTO
from site_project.domain.entities.news import News


class ICoordinator(ABC):
    @classmethod
    @abstractmethod
    def create(cls, coordinator_dto: CoordinatorCreationDTO):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_user(cls, email: str):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def update(cls, coordinator_id: UUID, coordinator):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def delete(cls, coordinator):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def publish_news(cls, news: News):
        raise NotImplementedError
