from abc import ABC, abstractmethod


class IStudentRepository(ABC):
    @abstractmethod
    @classmethod
    async def create(cls, StudentDTO):
        raise NotImplementedError
    
    @abstractmethod
    @classmethod
    async def update(cls, StudentDTO):
        raise NotImplementedError
    
    @abstractmethod
    @classmethod
    async def delete(cls, StudentDTO):
        raise NotImplementedError
    
    