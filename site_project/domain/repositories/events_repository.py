
from abc import ABC, abstractmethod
from site_project.domain.entities.event import Event


class IEventRepository(ABC):
    @classmethod
    @abstractmethod
    def create_event(cls, news: Event):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_event_by_id(cls, news_id):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def delete_event(cls, news_id):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def update_event(cls, news_id, news):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def list_event(cls):
        raise NotImplementedError
