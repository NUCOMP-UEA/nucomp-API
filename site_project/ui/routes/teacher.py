from fastapi import  APIRouter,status
import os

from fastapi import Depends
from site_project.domain.entities.student import Student
from site_project.application.dtos.creation_dto import StudentCreationDTO, StudentLoginDTO
from site_project.application.services.student import StudentService
from site_project.utils.authentication import create_access_token, decode_access_token
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer

# Create an instance of APIRouter
teacher_router= APIRouter(
    prefix=os.getenv("API_ROUTER_PREFIX", "/nucomp")
)


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = os.getenv('SECRET_KEY')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@teacher_router.get("/")
async def read_root():
    return {"message": "Hello, this is the root endpoint!"}

@teacher_router.post("/signup",response_model=Student,status_code=status.HTTP_201_CREATED)
async def create_student(student:StudentCreationDTO):
    await StudentService.signup(student)

@teacher_router.post("/login/",response_model=StudentLoginDTO)
async def login(student_login:StudentLoginDTO):
    return await StudentService.login(student_login)

    
@teacher_router.delete("delete")
async def delete(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    username = payload.get("sub")
    await StudentService.