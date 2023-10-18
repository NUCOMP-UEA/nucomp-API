import os

from fastapi import APIRouter, Depends, status

from site_project.application.dtos.creation_dto import CoordinatorCreationDTO
from site_project.application.dtos.update_dto import UserUpdateDTO
from site_project.application.services.coordinator import CoordinatorService
from fastapi import FastAPI, File, UploadFile, Form 
from site_project.ui.routes.utils.forms import get_coordinator_form
coordinator_router = APIRouter(prefix=os.getenv("API_ROUTER_PREFIX_CORD"))


@coordinator_router.post(
    "/signup/{user_id}",
    # response_model=CoordinatorCreationDTO,
    status_code=status.HTTP_201_CREATED
)
async def create(user_id:str, coordinator=Depends(get_coordinator_form)):
    
    return await CoordinatorService.signup(user_id, coordinator)


@coordinator_router.get("/coordinator-user/{coordinator_id}")
async def get_user(coordinator_id):
    return await CoordinatorService.get_user_by_id(coordinator_id)


@coordinator_router.delete("/delete")
async def delete(current_student=Depends(CoordinatorService.get_current_user)):
    return await CoordinatorService.delete(current_student)


@coordinator_router.put("/update")
async def update_user(
    user_data: UserUpdateDTO,
    current_user: UserUpdateDTO = Depends(CoordinatorService.get_current_user),
):
    return await CoordinatorService.update(current_user, user_data)
