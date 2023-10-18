from site_project.infra.database.articles import ArticleRepository
from site_project.domain.entities.article import Article


class ArticleService:
    @classmethod
    async def create_article(cls, article_creation_dto):
        article = Article(**article_creation_dto.dict())
        await ArticleRepository.create_article(article)

    @classmethod
    async def update_article(cls, article_id, article_updated_dto):
        article = await ArticleRepository.get_article_by_id(article_id)
        if article_updated_dto.authors is not None:
            article['authors'] = article_updated_dto.authors
        if article_updated_dto.title is not None:
            article['title'] = article_updated_dto.title
        if article_updated_dto.published_in is not None:
            article['published_in'] = article_updated_dto.published_in
        if article_updated_dto.published_at is not None:
            article['published_at'] = article_updated_dto.published_at
        if article_updated_dto.article_url is not None:
            article['article_url'] = article_updated_dto.article_url
            
        await ArticleRepository.update_article(article_id,article)
            

    @classmethod
    async def get_article(cls, article_id):
        return await ArticleRepository.get_article_by_id(article_id)

    @classmethod
    async def delete_article(cls, article_id):
        await ArticleRepository.delete_article(article_id)

    @classmethod
    async def list_all_articles(cls, page, per_page):
        skip = (page - 1) * per_page
        articles = await ArticleRepository.list_articles(skip, page)
        result = list(articles)
        return result 
