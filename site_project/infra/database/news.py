from abc import ABC, abstractmethod
from site_project.domain.entities.news import News
from site_project.domain.repositories.news_repository import INewsRepository
from site_project.infra.database.base import DatabaseMeta


class NewsRepository(INewsRepository, metaclass=DatabaseMeta):
    collection_name = "news"
    collection = None
    
    @classmethod
    async def get_news_by_id(cls, news_id):
        return await cls.collection.find_one(dict(id_=news_id))
    @classmethod
    async def create_news(cls, news: News):
        await cls.collection.insert_one(news.dict())

    @classmethod
    async def delete_news(cls, news_id):
        await cls.collection.delete_one(dict(id_=news_id))

    @classmethod
    async def update_news(cls, news_id, news):
        await cls.collection.replace_one(dict(id_=news_id),news)

    @classmethod
    async def list_news(cls):
        pipeline = [
            {
                "$project": {
                    "_id": 0,
                    "id_": 1,
                    "title": 1,
                    "caption": 1,
                    "image": 1,
                    "name": 1,
                    "published_at": 1,
                    "published_by": 1,
                    "tags": 1,
                   
                }
            }
        ]
        
        # print(cls.collection.find().to_list(length=None))
     
       
        return await cls.collection.aggregate(pipeline).to_list(length=None)
