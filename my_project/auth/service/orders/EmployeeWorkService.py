from my_project.auth.dao import Employee_work_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.EmployeeWork import EmployeeWork


class EmployeeWorkService(GeneralService):
    _dao = Employee_work_dao
