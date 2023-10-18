import os
from fastapi import APIRouter, Depends, Query
from site_project.domain.entities.news import News
from site_project.application.services.coordinator import CoordinatorService
from site_project.application.services.teacher import TeacherService
from site_project.application.services.articles_service import ArticleService
from site_project.application.dtos.creation_dto import ArticleCreationDTO
from site_project.application.dtos.update_dto import ArticleUpdateDTO
from site_project.domain.entities.article import Article
from site_project.domain.entities.teacher import Teacher
from site_project.domain.entities.coordinator import Coordinator
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List, Union
from fastapi import HTTPException


articles_router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX_ARTICLE"))


@articles_router.post("/creation/")
async def article_creation(
    article: ArticleCreationDTO,
    current_user: Union[Coordinator, Teacher] = Depends(
        CoordinatorService.get_current_user
    )
    
    or Depends(TeacherService.get_current_user)
):
  
    if current_user is None:
        raise HTTPException(status_code=403, detail="Not authorized")
    try:
        await ArticleService.create_article(article)
    except:
        raise HTTPException(
            status_code=500, detail="It was not possible to publish the news."
        )
    
    response = {"message": "article was successfully created"}
    return JSONResponse(status_code=201, content=response)


@articles_router.get("/list/", response_model=List[Article])
async def get_articles(page: int = Query(1, description="Page number", ge=1), per_page: int = Query(10, description="Items per page", le=100)):
    articles = ArticleService.list_all_articles(page, per_page)
    return await articles


@articles_router.patch("/update/")
async def update_news(
    article_id:str,
    updated_article:ArticleUpdateDTO,
    current_user: Union[Coordinator, Teacher] = Depends(
        CoordinatorService.get_current_user
    )
    or Depends(TeacherService.get_current_user),
):
    if current_user is None:
        raise HTTPException(status_code=403, detail="Not authorized")

    try:
        await ArticleService.update_article(article_id,updated_article)

    except:
        raise HTTPException(
            status_code=500, detail="It was not possible to update the article."
        )

    response = {"message": "article was successfully updated"}
    return JSONResponse(status_code=200, content=response)


@articles_router.delete("/delete/{article_id}")
async def delete_article(article_id: str,
        current_user: Union[Coordinator, Teacher] = Depends(
        CoordinatorService.get_current_user
    )
    or Depends(TeacherService.get_current_user)):
   
    article = await ArticleService.get_article(article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article was not found")

    try:
        await ArticleService.delete_article(article_id)

    except:
        raise HTTPException(
            status_code=500, detail="An error occurred while deleting the article."
        )
    response = {"message": "Article was successfully deleted"}
    return JSONResponse(status_code=200, content=response)


