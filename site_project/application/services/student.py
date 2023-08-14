import os
from datetime import datetime, timedelta

import jwt
from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from site_project.domain.entities.student import Student
from site_project.infra.database.student import StudentRepository
from site_project.utils.authentication import (create_access_token,
                                               decode_access_token)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="nucomp/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class StudentService:
    async def get_current_user(token: str = Depends(oauth2_scheme)):
        user = None
        payload = decode_access_token(token)
        email = payload.get("sub")
        user = await StudentRepository.get_user(email)

        if user:
            return user
        return None

    async def get_user_by_id(cls, user_id):
        user = await StudentRepository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @classmethod
    async def signup(cls, user_id, student_signup_dto):
        user = await StudentRepository.get_user_by_id(user_id)
        student = Student.to_student(user, student_signup_dto)
        student.id_ = str(student.id_)
        await StudentRepository.update(user_id, student)
        message = {"message": "user successfully created"}
        response = JSONResponse(content=message)
        return response

    @classmethod
    async def update_student(cls, current_user, new_data):
        student_id = current_user["id_"]
        return await StudentRepository.update(student_id, new_data)

    @classmethod
    async def delete_student(cls, student):
        await StudentRepository.delete(student)
        return {"message": "Student deleted"}
