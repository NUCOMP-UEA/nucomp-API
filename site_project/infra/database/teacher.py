# from site_project.application.dtos.creation_dto import TeacherCreationDTO
from site_project.domain.repositories.teacher_repository import ITeacherRepository
from site_project.infra.database.base import DatabaseMeta
from site_project.infra.database.utils.criation_utils import update_info


class TeacherRepository(ITeacherRepository, metaclass=DatabaseMeta):
    collection_name = "teacher"
    collection = None

    @classmethod
    async def create(cls, teacher, pwd_context):
        password = teacher.password
        teacher_dict = update_info(teacher)
        teacher_dict["password"] = pwd_context.hash(password)
        await cls.collection.insert_one(teacher_dict)

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
    async def update(cls, teacher_id, new_data):
        new_data.lattes_cv = str(new_data.lattes_cv)
        new_data.personal_site = str(new_data.personal_site)
        new_data.curriculum_lattes_url = str(new_data.curriculum_lattes_url)
        await cls.collection.replace_one(dict(id_=teacher_id), dict(new_data))

    @classmethod
    async def delete(cls, teacher):
        email = teacher["email"]
        return cls.collection.delete_one(dict(email=email))
