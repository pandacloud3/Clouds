
from my_project.auth.service import meteostation_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.Meteostation import Meteostation


class MeteostationController(GeneralController):
    _service = meteostation_service