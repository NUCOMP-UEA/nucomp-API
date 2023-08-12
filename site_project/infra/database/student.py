from site_project.domain.repositories.student_repository import IStudentRepository
from motor.motor_asyncio import AsyncIOMotorClient
from site_project.infra.database.base import Settings,DatabaseMeta
import os
import bcrypt

class StudentRepository(IStudentRepository, metaclass=DatabaseMeta):
    collection_name = 'student'
    collection = None
    
    @classmethod
    async def create(cls,student):
        password = student.password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        student.password = str(hashed_password)
        await cls.collection.insert_one(student.dict())

    @classmethod
    async def get_student(cls, email):
        return await cls.collection.find_one(dict(email=email))
    
    @classmethod
    async def update(cls,student):
        return await cls.collection.replace_one(student.dict())
        
    
    
    
    