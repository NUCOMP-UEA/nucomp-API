from motor.motor_asyncio import AsyncIOMotorClient
from abc import ABCMeta
import pymongo
import os

# class Settings(type):
#     _instance = None
#     def __new__(cls,*args,**kwargs):
#         client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
#         db = client.project
#         collection = db.student
#         kwargs['collection'] = collection
#         cls._instance = super().__new__(cls,*args,**kwargs)

#         return cls._instance


class Settings(type):
    _instance = None
    
    def __new__(cls, name, bases, attrs):
        if cls._instance is None:
            client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
            db = client.project
            collection = db.student
            attrs['collection'] = collection
            cls._instance = super().__new__(cls, name, bases, attrs)
        return cls._instance

    
class DatabaseMeta(Settings,ABCMeta):
    pass