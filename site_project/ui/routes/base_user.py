import os

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# from site_project.domain.entities.base import BaseUser
from site_project.application.dtos.creation_dto import BaseDTO
from site_project.application.services.user_creation import UserCreation
from site_project.application.services.user_login import UserLogin

nucomp_router = APIRouter(prefix="/nucomp")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@nucomp_router.get("/")
async def read_root():
    return {"message": "Hello, this is the root endpoint!"}


@nucomp_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: BaseDTO):
    return await UserCreation.signup(user)


@nucomp_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password
    return await UserLogin.login(email, password)


@nucomp_router.post("/password-reset")
async def reset_password(email: str, password: str, confirmation_password: str):
    if confirmation_password == password:
        await UserLogin.reset_password(email, password)
