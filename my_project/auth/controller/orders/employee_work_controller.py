from my_project.auth.service import employee_work_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.EmployeeWork import EmployeeWork


class EmployeeWorkController(GeneralController):
    _service = employee_work_service