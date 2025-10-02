from my_project.auth.service import gender_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.Gender import Gender


class GenderController(GeneralController):
    _service = gender_service