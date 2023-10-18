import os

from fastapi import APIRouter, Depends, status, Query

from site_project.application.services.coordinator import CoordinatorService
from site_project.application.services.news_service import NewsService
from site_project.application.dtos.creation_dto import NewsDTO
from site_project.application.dtos.update_dto import NewsUpdateDTO
from fastapi import FastAPI, File, UploadFile
from site_project.domain.entities.news import News
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import HTTPException

news_router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX_NEWS"))


@news_router.post("/news-creation/", status_code=status.HTTP_201_CREATED)
async def news_criation(
    news: NewsDTO, image: UploadFile = File(...), current_user=Depends(CoordinatorService.get_current_user)
):  
    
    file = image.file.read()
    if current_user is None:
        raise HTTPException(status_code=403, detail="Not authorized")
    try:
        await NewsService.publish_news(news, file)
    except:
        raise HTTPException(
            status_code=500, detail="It was not possible to publish the news."
        )
    response = {"message": "News successfully created"}

    return JSONResponse(status_code=201, content=response)


@news_router.get("/news-listing/", response_model=List[News])
async def get_news(page: int = Query(1, description="Page number", ge=1), per_page: int = Query(10, description="Items per page", le=100)):
    news = await NewsService.get_all_news(page, per_page)
    return news

@news_router.patch("/news-update/")
async def update_news(new_id, news:NewsUpdateDTO):
    await NewsService.update_news(new_id, news)
    response = {"message": "News successfully updated"}

    return JSONResponse(status_code=200, content=response)


@news_router.delete("/delete/{news_id}")
async def delete_news(news_id: str):
    news = await NewsService.get_news(news_id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")

    try:
        await NewsService.delete_news(news_id)

    except:
        raise HTTPException(
            status_code=500, detail="An error occurred while deleting the news."
        )
