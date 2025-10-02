from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.EmployeeWork import EmployeeWork


class EmployeeWorkDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для зв’язку між працівниками та сервісними роботами (EmployeeWork).
    """
    _domain_type = EmployeeWork

    def create(self, employee_work: EmployeeWork) -> None:
        """
        Додає новий запис у зв’язок EmployeeWork.
        :param employee_work: об’єкт EmployeeWork
        """
        self._session.add(employee_work)
        self._session.commit()

    def find_all(self) -> List[EmployeeWork]:
        """
        Отримує всі записи з EmployeeWork.
        :return: список усіх зв’язків
        """
        return self._session.query(EmployeeWork).all()

    def find_by_employee(self, employee_id: int) -> List[EmployeeWork]:
        """
        Отримує всі роботи, які виконував певний працівник.
        :param employee_id: ID працівника
        :return: список зв’язків EmployeeWork
        """
        return self._session.query(EmployeeWork).filter(EmployeeWork.employee_id == employee_id).all()

    def find_by_work(self, work_id: int) -> List[EmployeeWork]:
        """
        Отримує всіх працівників, які брали участь у певній роботі.
        :param work_id: ID сервісної роботи
        :return: список зв’язків EmployeeWork
        """
        return self._session.query(EmployeeWork).filter(EmployeeWork.work_id == work_id).all()

    def find_pair(self, employee_id: int, work_id: int) -> EmployeeWork:
        """
        Отримує конкретний запис за парою (employee_id, work_id).
        :param employee_id: ID працівника
        :param work_id: ID роботи
        :return: об’єкт EmployeeWork або None
        """
        return (self._session.query(EmployeeWork)
                .filter(EmployeeWork.employee_id == employee_id, EmployeeWork.work_id == work_id)
                .first())
