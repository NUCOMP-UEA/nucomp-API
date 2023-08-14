import os

from fastapi import APIRouter, Depends, Response, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from site_project.application.dtos.creation_dto import CoordinatorCreationDTO
from site_project.application.dtos.update_dto import UserUpdateDTO
from site_project.application.services.coordinator import CoordinatorService
from site_project.utils.authentication import (create_access_token,
                                               decode_access_token)

coordinator_router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX", "/nucomp"))


@coordinator_router.post(
    "/signup/coordinator/{user_id}",
    response_model=CoordinatorCreationDTO,
    status_code=status.HTTP_201_CREATED,
)
async def create(user_id, coordinator: CoordinatorCreationDTO):
    return await CoordinatorService.signup(user_id, coordinator)


@coordinator_router.get("/coordinator/{teacher_id}")
async def get_user(teacher_id):
    return await CoordinatorService.get_user_by_id(teacher_id)


@coordinator_router.delete("/coordinator/delete")
async def delete(current_student=Depends(CoordinatorService.get_current_user)):
    return await CoordinatorService.delete(current_student)


@coordinator_router.put("/coordinator/update")
async def update_user(
    user_data: UserUpdateDTO,
    current_user: UserUpdateDTO = Depends(CoordinatorService.get_current_user),
):
    return await CoordinatorService.update(current_user, user_data)
