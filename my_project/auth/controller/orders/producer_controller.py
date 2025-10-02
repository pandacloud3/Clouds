from my_project.auth.service import producer_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.Meteostation import Meteostation


class ProducerController(GeneralController):
    _service = producer_service