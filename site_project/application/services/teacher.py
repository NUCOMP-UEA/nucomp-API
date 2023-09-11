import os

from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse

from site_project.domain.entities.teacher import Teacher
from site_project.infra.database.teacher import TeacherRepository
from site_project.settings.authentication_settings import AuthenticationSettings
from site_project.utils.authentication import decode_access_token


class TeacherService:
    @staticmethod
    async def get_current_user(
        token: str = Depends(AuthenticationSettings.oauth2_scheme),
    ):
        user = None
        payload = decode_access_token(token)
        email = payload.get("sub")
        user = await TeacherRepository.get_user(email)

        if user:
            return user

        return None

    @staticmethod
    async def get_user(user_id):
        user = await TeacherRepository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    async def authenticate_user(student, password):
        response = AuthenticationSettings.pwd_context.verify(
            password, student["password"]
        )
        return response

    @classmethod
    async def signup(cls, user_id, teacher_signup_dto):
        user = await TeacherRepository.get_user(user_id)
        student = Teacher.to_teacher(user, teacher_signup_dto)
        student.id_ = str(student.id_)
        await TeacherRepository.update(user_id, student)
        message = {"message": "user successfully created"}
        response = JSONResponse(content=message)
        return response

    @classmethod
    async def update(cls, current_user, new_data):
        student_id = current_user["id_"]
        await TeacherRepository.update(student_id, new_data)

    @classmethod
    async def delete(cls, teacher):
        await TeacherRepository.delete(teacher)
        return {"message": "User deleted"}
