from abc import ABC, abstractmethod
from site_project.infra.database.base import Settings
class IStudentRepository(ABC):
    
    @classmethod
    @abstractmethod
    def create(cls, student_dto):
        raise NotImplementedError
    
    
    @classmethod
    @abstractmethod
    def update(cls, student_dto):
        raise NotImplementedError
    
    
    @classmethod
    @abstractmethod
    def delete(cls, student_dto):
        raise NotImplementedError
    
    