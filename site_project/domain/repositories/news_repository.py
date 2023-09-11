from abc import ABC, abstractmethod
from site_project.domain.entities.news import News


class INewsRepository(ABC):
    @classmethod
    @abstractmethod
    def create_news(cls, news: News):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_news_by_id(cls, news_id):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def delete_news(cls, news_id):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def update_news(cls, news_id, news):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def list_news(cls):
        raise NotImplementedError
