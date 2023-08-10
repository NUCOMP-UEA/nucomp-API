
from site_project.application.dtos.creation_dto import TeacherDTO
from abc import ABC, abstractmethod


class ITeacherRepository(ABC):
    @abstractmethod
    @classmethod
    async def create(cls,teacher:TeacherDTO):
        raise NotImplementedError
    
    @abstractmethod
    @classmethod
    async def get_teacher(cls, teacher):
        return NotImplementedError
    
    @abstractmethod
    @classmethod
    async def update(cls,teacher):
        return NotImplementedError
    
    @abstractmethod
    @classmethod
    async def delete(cls,teacher_id):
        return NotImplementedError
    