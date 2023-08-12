from site_project.infra.database.student import StudentRepository
from fastapi import FastAPI, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
import jwt
from site_project.utils.authentication import create_access_token, decode_access_token

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class StudentService:
    @staticmethod
    async def authenticate_user(student, student_login_dto):
        response = pwd_context.verify(student['password'], student_login_dto.password)
        return response
    
    @classmethod
    async def signup(cls,student_signup_dto):
        name = student_signup_dto.name
        student = await StudentRepository.get_student(name)
        if student:
            raise HTTPException(status_code=409, detail="Username already exists")
        
        await StudentRepository.create(student_signup_dto)
        message = {"message": "user successfully created"}
        response = JSONResponse(content=message)
        return response

    @classmethod
    async def login(cls, student_login_dto):
        student = await StudentRepository.get_student(student_login_dto.email)
        
        if student is None or not await cls.authenticate_user(student,student_login_dto):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        print(student)
        access_token = create_access_token(
            data={"sub": student["username"]}, expires_delta=access_token_expires
        )
        response = Response()
        response.set_cookie(key="access_token", value=access_token, expires=access_token_expires.total_seconds(), httponly=True)
        return response

    
    
    
    async def update_student(cls,student):
        await StudentRepository.update(dict(student))



