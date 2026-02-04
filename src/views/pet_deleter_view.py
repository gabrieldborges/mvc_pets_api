from src.controllers.interfaces.pet_deleter_controller_interface import PetDeleterControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface


class PetDeleterrView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_request = http_request.param["pet_name"]
        self.__controller.delete(body_request)
        return HttpResponse(status_code=204)