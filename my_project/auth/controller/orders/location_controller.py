from my_project.auth.service import location_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.Location import Location


class LocationController(GeneralController):
    _service = location_service