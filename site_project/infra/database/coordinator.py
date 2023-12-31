from site_project.domain.repositories.coordinator import ICoordinator
from site_project.infra.database.base import DatabaseMeta
from site_project.infra.database.utils.criation_utils import update_info
from site_project.domain.entities.base import BaseUser

class CoordinatorRepository(ICoordinator, metaclass=DatabaseMeta):
    collection_name = "coordinator"
    collection = None

    @classmethod
    async def create(cls, coordinator, pwd_context):
        base_user = BaseUser(**coordinator.dict())
        
        password = coordinator.password
        coordinator_dict = update_info(base_user)
        coordinator_dict["password"] = pwd_context.hash(password)
        await cls.collection.insert_one(coordinator_dict)
        return coordinator_dict

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
        new_data_dict = dict(new_data)
        del new_data_dict['photo']
        await cls.collection.replace_one(dict(_id=student_id), new_data_dict)

    @classmethod
    async def delete(cls, coordinator):
        email = coordinator["email"]
        return cls.collection.delete_one(dict(email=email))
