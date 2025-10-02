from my_project.auth.dao import Employee_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Employee import Employee


class EmployeeService(GeneralService):
    _dao = Employee_dao
