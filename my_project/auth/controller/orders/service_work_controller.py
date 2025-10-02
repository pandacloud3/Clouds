
from my_project.auth.service import service_work_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.ServiceWork import ServiceWork


class ServiceWorkController(GeneralController):
    _service = service_work_service