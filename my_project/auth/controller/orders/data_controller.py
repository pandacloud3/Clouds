from my_project.auth.service import data_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.Data import Data


class DataController(GeneralController):
    _service = data_service