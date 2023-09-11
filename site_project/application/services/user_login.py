import os
from datetime import timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from site_project.infra.database.coordinator import CoordinatorRepository
from site_project.infra.database.student import StudentRepository
from site_project.infra.database.teacher import TeacherRepository
from site_project.utils.authentication import create_access_token, decode_access_token
from site_project.settings.authentication_settings import AuthenticationSettings


class UserLogin:
    @classmethod
    async def get_current_user(
        cls, token: str = Depends(AuthenticationSettings.oauth2_scheme)
    ):
        user = None
        payload = decode_access_token(token)
        email = payload.get("sub")
        user = await cls.get_user(email)
        if user:
            return user
        return None

    @staticmethod
    async def authenticate_user(student, password):
        response = AuthenticationSettings.pwd_context.verify(
            password, student["password"]
        )
        return response

    @staticmethod
    async def get_user(email: str):
        repositories = [StudentRepository, CoordinatorRepository, TeacherRepository]
        for repository in repositories:
            user = await repository.get_user(email)
            if user:
                return user
        return None

    @classmethod
    async def reset_password(cls, email: str, new_password: str):
        user = await cls.get_user(email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        user["password"] = str(AuthenticationSettings.pwd_context.hash(new_password))
        await StudentRepository.update_password(user["id_"], user)
        await CoordinatorRepository.update_password(user["id_"], user)
        await TeacherRepository.update_password(user["id_"], user)

    @classmethod
    async def login(cls, email, password):
        user = await cls.get_user(email)
        if user is None or not await cls.authenticate_user(user, password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        access_token_expires = timedelta(
            minutes=AuthenticationSettings.access_token_expire_minutos
        )
        access_token = create_access_token(
            data={"sub": user["email"]}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
