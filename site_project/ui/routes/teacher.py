import os

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from site_project.application.dtos.creation_dto import TeacherCreationDTO
from site_project.application.services.teacher import TeacherService
from site_project.domain.entities.teacher import Teacher

# Create an instance of APIRouter
teacher_router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX", "/nucomp"))


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
SECRET_KEY = os.getenv("SECRET_KEY")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@teacher_router.post(
    "/signup/teacher/{user_id}",
    response_model=TeacherCreationDTO,
    status_code=status.HTTP_201_CREATED,
)
async def create_teacher(user_id, teacher: TeacherCreationDTO):
    return await TeacherService.signup(user_id, teacher)


@teacher_router.delete("/teacher/delete")
async def delete(current_student=Depends(TeacherService.get_current_user)):
    if current_student is not None:
        return await TeacherService.delete(current_student)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found.",
    )


@teacher_router.get("/teacher/{teacher_id}")
async def get_user(teacher_id):
    return await TeacherService.get_user_by_id(teacher_id)


@teacher_router.put("/teacher/update/")
async def update_user(
    user_data: Teacher, current_user: Teacher = Depends(TeacherService.get_current_user)
):
    if current_user is not None:
        return await TeacherService.update(current_user, user_data)
    else:
        raise HTTPException(status_code=403, detail="Not authorized")
