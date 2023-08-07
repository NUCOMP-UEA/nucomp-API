from abc import ABC, abstractmethod
from site_project.domain.entities.student import StudentDTO

class IStudentRepository(ABC):
    @abstractmethod
    @classmethod
    def create(cls, StudentDTO):
        raise NotImplementedError
    
    @abstractmethod
    @classmethod
    def update(cls, StudentDTO):
        raise NotImplementedError
    
    @abstractmethod
    @classmethod
    def delete(cls, StudentDTO):
        raise NotImplementedError
    
    