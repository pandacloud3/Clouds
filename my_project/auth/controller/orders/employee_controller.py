from my_project.auth.service import employee_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.Employee import Employee


class EmployeeController(GeneralController):
    _service = employee_service