

from sqlalchemy import Column, String, BIGINT, ForeignKey
from src.models.sqlite.settings.base import Base

class PeopleTable(Base):
    '''sumary'''
    def __init__(self) -> None:
        pass

    __tablename = 'people'

    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, ForeignKey("pets.id"),nullable=False)

    
    
    def __repr__(self):
        return f"{self.__tablename} [name={self.first_name},last name={self.last_name} age={self.age}, petID={self.pet_id}]"
