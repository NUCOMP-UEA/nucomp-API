from site_project.application.infra.database.student import StudentRepository
from fastapi import FastAPI, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta

from site_project.utils.authentication import create_access_token, decode_access_token
import os

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")




class StudentService:
    
    @classmethod
    async def signup(cls,student):
        await StudentRepository.create(student)

    @classmethod
    async def login(cls, student_login_dto):
        student = await cls.authenticate_user(student_login_dto.username, student_login_dto.password)
        if not student:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": student["username"]}, expires_delta=access_token_expires
        )
        response = Response()
        response.set_cookie(key="access_token", value=access_token, expires=access_token_expires.total_seconds(), httponly=True)
        return response

    
    def authenticate_user(username: str, password: str):
        user_data = StudentRepository.get_student(username)
        if user_data and user_data["password"] == password:
            return user_data
    
    async def update_student(cls,student):
        await StudentRepository.update(dict(student))

    asynce def delete_student(cls,student):
        await StudentRepository.delete()



