from abc import ABC, abstractmethod
from site_project.domain.repositories.article_repository import IArticleRepository
from site_project.domain.entities.article import Article
from site_project.infra.database.base import DatabaseMeta

class ArticleRepository(IArticleRepository, metaclass=DatabaseMeta):
    collection_name = "article"
    collection = None

    @classmethod
    async def create_article(cls, article: Article):
        article.id_ = str(article.id_)
        await cls.collection.insert_one(article.dict())

    @classmethod
    async def get_article_by_id(cls, article_id):
        return await cls.collection.find_one(dict(id_=article_id))

    @classmethod
    async def delete_article(cls, article_id):
        print(article_id)
        await cls.collection.delete_one(dict(id_=article_id))

    @classmethod
    async def update_article(cls, article_id, article):
        await cls.collection.replace_one(dict(id_=article_id),article)

    @classmethod
    async def list_articles(cls):
        
        pipeline = [
            {
                "$project": {
                    "_id": 0,
                    "id_": 1,
                    "authors": 1,
                    "title": 1,
                    "published_in": 1,
                    "published_at": 1,
                    "published_by": 1,
                    "article_url": 1,
                   
                }
            }
        ]
       
        return await cls.collection.aggregate(pipeline).to_list(length=None)
    
