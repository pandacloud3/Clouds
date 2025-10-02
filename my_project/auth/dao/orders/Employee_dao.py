from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Employee import Employee


class EmployeeDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для працівників (Employee).
    """
    _domain_type = Employee

    def create(self, employee: Employee) -> None:
        """
        Додає нового працівника в базу даних.
        :param employee: об'єкт Employee
        """
        self._session.add(employee)
        self._session.commit()

    def find_all(self) -> List[Employee]:
        """
        Отримує всіх працівників.
        :return: список усіх Employee
        """
        return self._session.query(Employee).all()

    def find_by_id(self, employee_id: int) -> Employee:
        """
        Отримує працівника за його ID.
        :param employee_id: ID працівника
        :return: об'єкт Employee або None
        """
        return self._session.query(Employee).filter(Employee.id == employee_id).first()

    def find_by_email(self, email: str) -> Employee:
        """
        Отримує працівника за email.
        :param email: email працівника
        :return: об'єкт Employee або None
        """
        return self._session.query(Employee).filter(Employee.email == email).first()

    def find_by_last_name(self, last_name: str) -> List[Employee]:
        """
        Отримує всіх працівників з певним прізвищем.
        :param last_name: прізвище працівника
        :return: список Employee
        """
        return self._session.query(Employee).filter(Employee.last_name == last_name).all()

    def find_by_gender(self, gender_id: int) -> List[Employee]:
        """
        Отримує всіх працівників певної статі.
        :param gender_id: ID гендеру
        :return: список Employee
        """
        return self._session.query(Employee).filter(Employee.gender_id == gender_id).all()
