import os

import bcrypt
from passlib.context import CryptContext

from site_project.domain.repositories.student_repository import \
    IStudentRepository
from site_project.infra.database.base import DatabaseMeta
from site_project.utils.authentication import (create_access_token,
                                               decode_access_token)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class StudentRepository(IStudentRepository, metaclass=DatabaseMeta):
    collection_name = "student"
    collection = None

    @classmethod
    async def create(cls, student, pwd_context):
        password = student.password
        student_dict = student.dict()
        student_dict["id_"] = str(student_dict["id_"])
        hashed_password = pwd_context.hash(password)
        student_dict["password"] = hashed_password
        del student_dict["user_type"]
        await cls.collection.insert_one(student_dict)

    @classmethod
    async def get_user_by_id(cls, user_id):
        return await cls.collection.find_one(dict(id_=user_id))

    @classmethod
    async def update_password(cls, teacher_id, new_data):
        await cls.collection.replace_one(dict(id_=teacher_id), dict(new_data))

    @classmethod
    async def get_user(cls, email):
        return await cls.collection.find_one(dict(email=email))

    @classmethod
    async def update(cls, student_id, new_data):
        await cls.collection.replace_one(dict(id_=student_id), dict(new_data))

    @classmethod
    async def delete(cls, student):
        email = student["email"]
        return cls.collection.delete_one(dict(email=email))
