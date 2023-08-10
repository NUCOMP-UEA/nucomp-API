from site_project.domain.repositories.teacher_repository import ITeacherRepository
from motor.motor_asyncio import AsyncIOMotorClient
from site_project.application.dtos.creation_dto import TeacherDTO
from site_project.infra.database.base import Settings
import os

class TeacherRepository(ITeacherRepository, metaclass=Settings):
    collection_name = 'teacher'
    collection = None
    
    @classmethod
    async def create(cls,teacher:TeacherDTO):
        await cls.collection.insert_one(teacher)

    @classmethod
    async def get_student(cls, teacher):
        return await cls.collection.find_one(teacher.dict())
    
    @classmethod
    async def update(cls,teacher):
        await cls.collection.replace_one(teacher.dict())
    
    @classmethod
    async def delete(cls,teacher_id):
        return cls.collection.delete_one(id=teacher_id)