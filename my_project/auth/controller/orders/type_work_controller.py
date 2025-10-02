
from my_project.auth.service import type_work_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.TypeWork import TypeWork


class TypeWorkController(GeneralController):
    _service = type_work_service