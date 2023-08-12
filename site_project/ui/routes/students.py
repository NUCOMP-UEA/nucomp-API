from fastapi import  APIRouter,status
import os

from fastapi import Depends,Response
from site_project.domain.entities.student import Student
from site_project.application.dtos.student_creation_dto import StudentCreationDTO, StudentLoginDTO
from site_project.application.services.student import StudentService
from site_project.utils.authentication import create_access_token, decode_access_token
from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer

# Create an instance of APIRouter
student_router= APIRouter(
    prefix=os.getenv("API_ROUTER_PREFIX", "/nucomp")
)

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@student_router.get("/")
async def read_root():
    return {"message": "Hello, this is the root endpoint!"}

@student_router.post("/signup",response_model=Student,status_code=status.HTTP_201_CREATED)
async def create_student(student:StudentCreationDTO):
    return await StudentService.signup(student)
    

@student_router.post("/login/",response_model=StudentLoginDTO)
async def login(student_login:StudentLoginDTO):
    return await StudentService.login(student_login)

    
@student_router.delete("/delete")
async def delete(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    username = payload.get("sub")
