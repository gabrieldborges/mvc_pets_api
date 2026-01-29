from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="fluffy", type="maltes", id=4),
            PetsTable(name="buddy", type="dalmata", id=5),
        ]


def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"pet_name": "fluffy", "pet_type": "maltes", "pet_id": 4},
                {"pet_name": "buddy", "pet_type": "dalmata", "pet_id": 5},
            ],
        }
    }

    assert response == expected_response
