from typing import List
from src.models.sqlite.interfaces.pets_repository_interface import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable
from .interfaces.pet_lister_controller_interface import PetListerControllerInterface

class PetListerController(PetListerControllerInterface):
    def __init__(self, pet_repository : PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository


    def list(self) -> dict:
        pets = self.__get_pets_in_database()
        response = self.__format_response(pets)
        return response


    def __get_pets_in_database (self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets : List[PetsTable]) -> dict:
        formatted_pets = []

        for pet in pets:
            formatted_pets.append({
                "pet_name" : pet.name,
                "pet_type" : pet.type,
                "pet_id" : pet.id   
            })
        return {
            "data" : {
                "type" : "Pets",
                "count" : len(formatted_pets),
                "attributes" : formatted_pets 
            }
        }