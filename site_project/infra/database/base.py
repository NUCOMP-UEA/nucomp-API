from motor.motor_asyncio import AsyncIOMotorClient
import pymongo
import os

class Settings:
    _instance = None
    def __new__(cls,*args,**kwargs):
        client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
        db = client.project
        collection = db.student
        kwargs['collection'] = collection
        
        if not cls._instance:
            cls._instance = super().__new__(cls,*args,**kwargs)
            return cls._instance