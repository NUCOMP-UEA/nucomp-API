import os
from abc import ABCMeta

from motor.motor_asyncio import AsyncIOMotorClient


class Settings:
    _instance = {}

    def __new__(cls, name, bases, attrs):
        client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
        database = client.project
        collection = database[attrs.get("collection_name")]
        attrs["collection"] = collection
        cls._instance = super().__new__(cls, name, bases, attrs)
        return cls._instance


class DatabaseMeta(Settings, ABCMeta):
    pass
