from site_project.domain.repositories.coordinator import ICoordinator
from site_project.infra.database.base import DatabaseMeta


class CoordinatorRepository(ICoordinator, metaclass=DatabaseMeta):
    collection_name = "coordinator"
    collection = None

    @classmethod
    async def create(cls, coordinator, pwd_context):
        password = coordinator.password
        coordinator_dict = coordinator.dict()
        hashed_password = pwd_context.hash(password)
        coordinator_dict["password"] = hashed_password
        coordinator_dict["id_"] = str(coordinator_dict["id_"])
        del coordinator_dict["user_type"]
        await cls.collection.insert_one(coordinator_dict)

    @classmethod
    async def get_user_by_id(cls, user_id):
        return await cls.collection.find_one(dict(id_=user_id))

    @classmethod
    async def get_user(cls, email):
        return await cls.collection.find_one(dict(email=email))

    @classmethod
    async def update_password(cls, teacher_id, new_data):
        await cls.collection.replace_one(dict(id_=teacher_id), dict(new_data))

    @classmethod
    async def update(cls, student_id, new_data):
        await cls.collection.replace_one(dict(_id=student_id), dict(new_data))

    @classmethod
    async def delete(cls, coordinator):
        email = coordinator["email"]
        return cls.collection.delete_one(dict(email=email))
