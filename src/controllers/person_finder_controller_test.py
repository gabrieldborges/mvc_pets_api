#pylint: disable=unused-argument
import pytest
from .person_finder_controller import PersonFinderController

class MockPerson:
    def __init__(self, first_name, last_name, pet_name, pet_type) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type


class MockPeopleRepository:
    def get_person(self, person_id : int):
        return MockPerson(first_name="John", last_name="Doe", pet_name="Buddy", pet_type="Dog")
        

class MockPeopleRepositoryPersonNotFound:
    def get_person(self, person_id : int):
        pass

def test_find_person_not_found():
    person_id = 2
    with pytest.raises(Exception):
        PersonFinderController(MockPeopleRepositoryPersonNotFound()).find(person_id)

def test_find_person_found():
    person_id = 1 

    person = PersonFinderController(MockPeopleRepository()).find(person_id)

    assert person["data"]["type"] == "Person"
    assert person["data"]["count"] == 1
    assert person["data"]["attributes"] == {
        "first_name" : "John",
        "last_name" : "Doe",
        "pet_name" : "Buddy",
        "pet_type" : "Dog",
    }
