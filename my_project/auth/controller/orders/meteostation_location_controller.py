
from my_project.auth.service import meteostation_location_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.MeteostationLocation import MeteostationLocation


class MeteostationLocationController(GeneralController):
    _service = meteostation_location_service