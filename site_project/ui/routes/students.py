import os

from fastapi import APIRouter, Depends, HTTPException, status

from site_project.application.dtos.creation_dto import StudentCreationDTO
from site_project.application.dtos.update_dto import UserUpdateDTO
from site_project.application.services.student import StudentService
from site_project.domain.entities.student import Student

# Create an instance of APIRouter
student_router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX_STUDENT"))


@student_router.post(
    "/signup/{user_id}",
    response_model=StudentCreationDTO,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(user_id, student: StudentCreationDTO):
    return await StudentService.signup(user_id, student)


@student_router.delete("/delete")
async def delete(current_student=Depends(StudentService.get_current_user)):
    if current_student is not None:
        return await StudentService.delete_student(current_student)

    else:
        raise HTTPException(status_code=403, detail="Not authorized")


@student_router.get("/{student_id}")
async def get_user(student_id):
    return await StudentService.get_user_by_id(student_id)


@student_router.put("/update")
async def update_user(
    user_data: UserUpdateDTO,
    current_user: Student = Depends(StudentService.get_current_user),
):
    if current_user is not None:
        await StudentService.update_student(current_user, user_data)

    raise HTTPException(status_code=403, detail="Not authorized")
