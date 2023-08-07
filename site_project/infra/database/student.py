from site_project.domain.repositories.student_repository import IStudentRepository
from motor.motor_asyncio import AsyncIOMotorClient
from site_project.application.dtos.student_dto import StudentDTO
from site_project.infra.database.base import Settings
import os

class StudentDB(IStudentRepository, metaclass=Settings):
    collection_name = 'student'
    collection = None
    
    @classmethod
    async def create(cls,student:StudentDTO):
        await cls.collection.insert_one(student)
        
    
    
    
    