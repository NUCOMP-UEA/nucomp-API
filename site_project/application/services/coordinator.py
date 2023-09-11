from fastapi import Depends, HTTPException
from fastapi.responses import JSONResponse

from site_project.domain.entities.coordinator import Coordinator
from site_project.infra.database.coordinator import CoordinatorRepository
from site_project.settings.authentication_settings import AuthenticationSettings
from site_project.utils.authentication import decode_access_token


class CoordinatorService:
    @staticmethod
    async def get_current_user(
        token: str = Depends(AuthenticationSettings.oauth2_scheme),
    ):
        user = None
        payload = decode_access_token(token)
        email = payload.get("sub")
        user = await CoordinatorRepository.get_user(email)

        if user:
            return user
        return None

    @staticmethod
    async def get_user_by_id(cls, user_id):
        user = await CoordinatorRepository.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @classmethod
    async def signup(cls, user_id, coordinator_signup_dto):
        user = await CoordinatorRepository.get_user_by_id(user_id)
        coordinator = Coordinator.to_entity(user, coordinator_signup_dto)
        coordinator.id_ = str(coordinator.id_)
        await CoordinatorRepository.update(user_id, coordinator)
        message = {"message": "user successfully created"}
        response = JSONResponse(content=message)
        return response

    @classmethod
    async def update(cls, current_user, new_data):
        student_id = current_user["id_"]
        await CoordinatorRepository.update(student_id, new_data)

    @classmethod
    async def delete(cls, student):
        await CoordinatorRepository.delete(student)
        return {"message": "The user has been deleted"}
