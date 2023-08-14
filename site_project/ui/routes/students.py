import os

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from site_project.application.dtos.creation_dto import StudentCreationDTO
from site_project.application.dtos.update_dto import UserUpdateDTO
from site_project.application.services.student import StudentService
from site_project.domain.entities.student import Student
from site_project.utils.authentication import (create_access_token,
                                               decode_access_token)

# Create an instance of APIRouter
student_router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX", "/nucomp"))


ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = os.getenv("SECRET_KEY")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="nucomp/login")


@student_router.post(
    "/signup/student/{user_id}",
    response_model=StudentCreationDTO,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(user_id, student: StudentCreationDTO):
    return await StudentService.signup(user_id, student)


@student_router.delete("/student/delete")
async def delete(current_student=Depends(StudentService.get_current_user)):
    if current_student is not None:
        return await StudentService.delete_student(current_student)

    else:
        raise HTTPException(status_code=403, detail="Not authorized")


@student_router.get("/student/{student_id}")
async def get_user(student_id):
    return await StudentService.get_user_by_id(student_id)


@student_router.put("/student/update")
async def update_user(
    user_data: UserUpdateDTO,
    current_user: Student = Depends(StudentService.get_current_user),
):
    print(user_data)
    print(current_user)
    if current_user is not None:
        await StudentService.update_student(current_user, user_data)
    else:
        raise HTTPException(status_code=403, detail="Not authorized")
