from site_project.domain.repositories.student_repository import IStudentRepository
from motor.motor_asyncio import AsyncIOMotorClient
from site_project.application.dtos.creation_dto import StudentDTO
from site_project.infra.database.base import Settings
import os

class StudentRepository(IStudentRepository, metaclass=Settings):
    collection_name = 'student'
    collection = None
    
    @classmethod
    async def create(cls,student:StudentDTO):
        await cls.collection.insert_one(student)

    @classmethod
    async def get_student(cls, student):
        return await cls.collection.find_one(student.dict())
    
    @classmethod
    async def update(cls,student):
        await cls.collection.replace_one(student.dict())
    
    @classmethod
    async def delete(cls,student_id):
        return cls.collection.delete_one(id=student_id)
    
    
    
        
    
    
    
    