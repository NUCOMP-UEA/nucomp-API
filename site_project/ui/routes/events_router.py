import os

from fastapi import APIRouter, Depends, status, Query

from site_project.application.services.coordinator import CoordinatorService
from site_project.application.dtos.creation_dto import EventCreationDTO
from site_project.application.dtos.update_dto import EventUpdateDTO
from site_project.application.services.events_service import EventsService
# from site_project.application.services.
from site_project.domain.entities.event import Event
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from fastapi import HTTPException

events_router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX_EVENT"))


@events_router.post("/event-creation/", status_code=status.HTTP_201_CREATED)
async def create_events(
    event: EventCreationDTO, current_user=Depends(CoordinatorService.get_current_user)
):  
    await EventsService.create_event(event)
    if current_user is None:
        raise HTTPException(status_code=403, detail="Not authorized")
    try:
        await EventsService.create_event(event)
    except:
        raise HTTPException(
            status_code=500, detail="It was not possible to publish the news."
        )
    response = {"message": "event successfully created"}

    return JSONResponse(status_code=201, content=response)



@events_router.get("/events-listing/", response_model=List[Event])
async def get_events(page: int = Query(1, description="Page number", ge=1), per_page: int = Query(10, description="Items per page", le=100)):
    result = await EventsService.list_events(page, per_page)
    print(result)
    return result


@events_router.patch("/event-update/")
async def update_vent(event_id, event:EventUpdateDTO):
    await EventsService.update_event(event_id, event)
    response = {"message": "event was successfully updated"}

    return JSONResponse(status_code=200, content=response)


@events_router.delete("/delete/{news_id}")
async def delete_news(event_id: str):
    event = await EventsService.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event was not found")

    try:
        await EventsService.delete_event(event_id)

    except:
        raise HTTPException(
            status_code=500, detail="An error occurred while deleting the event."
        )
