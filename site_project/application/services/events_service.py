from site_project.domain.entities.event import Event
from site_project.infra.database.events import EventRepository



class EventsService:
    
    @classmethod
    async def create_event(cls, event_creation_dto):
        article = Event(**event_creation_dto.dict())
        await EventRepository.create_event(article)

    @classmethod
    async def update_event(cls, event_id, new_event):
        event = await EventRepository.get_event_by_id(event_id)
        if new_event.title is not None:
            event['title'] = new_event.title
        if new_event.image is not None:
            event['image'] = new_event.image
        if new_event.place is not None:
            event['place'] = new_event.place
        if new_event.date is not None:
            event['date'] = new_event.date
        if new_event.site_url is not None:
            event['site_url'] = new_event.site_url
            
        await EventRepository.update_event(event_id,event)
            

    @classmethod
    async def get_event(cls, event_id):
        return await EventRepository.get_event_by_id(event_id)

    @classmethod
    async def delete_event(cls, event_id):
        await EventRepository.delete_article(event_id)

    @classmethod
    async def list_events(cls,page, per_page):
        skip = (page - 1) * per_page
        items = await EventRepository.list_events(skip, page)
        result = list(items)
        return result