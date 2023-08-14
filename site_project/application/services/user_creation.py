from fastapi import HTTPException
from passlib.context import CryptContext

from site_project.application.dtos.creation_dto import BaseDTO
from site_project.domain.entities.base import TypeUser
from site_project.infra.database.coordinator import CoordinatorRepository
from site_project.infra.database.student import StudentRepository
from site_project.infra.database.teacher import TeacherRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserCreation:
    @classmethod
    async def signup(cls, user_creation_dto: BaseDTO):
        email = user_creation_dto.email
        user_type = user_creation_dto.user_type
        repository = await cls.get_repository(user_type)
        user = await repository.get_user(email)

        if user:
            raise HTTPException(status_code=409, detail="User already exists")

        await repository.create(user_creation_dto, pwd_context)
        created_user = await repository.get_user(email)
        message = {"user_id": str(created_user["id_"])}
        return message

    @staticmethod
    async def get_repository(user_type):
        if user_type == TypeUser.STUDENT.value:
            return StudentRepository
        elif user_type == TypeUser.COORDINATOR.value:
            return CoordinatorRepository

        elif user_type == TypeUser.TEACHER.value:
            return TeacherRepository
