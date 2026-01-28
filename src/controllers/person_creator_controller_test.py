import pytest
from .person_creator_controller import PersonCreatorController
class MockPeopleRepository:
    def insert_person(self, first_name : str, last_name : str, age : int, pet_id : int):
        pass


def test_create():
    controller = PersonCreatorController(MockPeopleRepository())

    person_info = {
        "first_name" : "John",
        "last_name" : "Doe",
        "age" : 30,
        "pet_id" : 4, 
    }

    response = controller.create(person_info)  

    assert response['data']["type"] == "Person"
    assert response['data']["count"] == 1
    assert response['data']["attributes"] == person_info

def test_create_invalid_person_info():
    controller = PersonCreatorController(MockPeopleRepository())

    person_info = {
        "first_name" : "John123",
        "last_name" : "Doe",
        "age" : 30,
        "pet_id" : 4, 
    }
    
    with pytest.raises(Exception):
        controller.create(person_info)