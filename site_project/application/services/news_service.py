from fastapi import Depends, HTTPException
from site_project.infra.database.news import NewsRepository
from site_project.domain.entities.news import News

class NewsService:
    @classmethod
    async def publish_news(cls, news):
        news = News(**news.dict())
        news.id_ = str(news.id_)
        await NewsRepository.create_news(news)

    @classmethod
    async def get_all_news(cls):
        return await NewsRepository.list_news()

    @classmethod
    async def get_news(cls, news_id):
        news = await NewsRepository.get_news_by_id(news_id)
        if news is None:
            raise HTTPException(status_code=404,detail="News not found")

        return news

    @classmethod
    async def delete_news(cls, news_id):
        await NewsRepository.delete_news(news_id)

    @classmethod
    async def update_news(cls, news_id, news_updated_dto):
        news = await cls.get_news(news_id)
        
        if news_updated_dto.title is not None:
            news['title'] = news_updated_dto.title
        if news_updated_dto.caption is not None:
            news['caption'] = news_updated_dto.caption
        if news_updated_dto.image is not None:
            news['image'] = news_updated_dto.image
        if news_updated_dto.tags is not None:
            news['tags'] = news_updated_dto.tags
                
        await NewsRepository.update_news(news_id,news)
