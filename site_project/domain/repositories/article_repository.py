from abc import ABC, abstractmethod
from site_project.domain.entities.news import News


class IArticleRepository(ABC):
    @classmethod
    @abstractmethod
    def create_article(cls, news: News):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_article_by_id(cls, news_id):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def delete_article(cls, news_id):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def update_article(cls, news_id, news):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def list_articles(cls):
        raise NotImplementedError
