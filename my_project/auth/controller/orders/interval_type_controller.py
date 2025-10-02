
from my_project.auth.service import interval_type_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.IntervalType import IntervalType


class IntervalTypeController(GeneralController):
    _service = interval_type_service