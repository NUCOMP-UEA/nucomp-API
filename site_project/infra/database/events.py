from site_project.domain.entities.event import Event
from site_project.domain.repositories.events_repository import IEventRepository
from site_project.infra.database.base import DatabaseMeta

class EventRepository(IEventRepository,metaclass=DatabaseMeta):
    collection_name = "events"
    collection = None
    
    @classmethod
    async def create_event(cls, event: Event):
        event.id_ = str(event.id_)
        await cls.collection.insert_one(event.dict())

    @classmethod
    async def get_event_by_id(cls, event_id):
        return cls.collection.find_one(dict(id_=event_id))

    @classmethod
    async def delete_event(cls, event_id):
        return cls.collection.delete_one(dict(id_=event_id))

    @classmethod
    async def update_event(cls, event_id, event):
        return cls.collection.replace_one(dict(id_=event_id),event)

    @classmethod
    async def list_events(cls,skip, per_page):
        events = await cls.collection.find().skip(skip).limit(per_page).to_list(length=None)
        return events