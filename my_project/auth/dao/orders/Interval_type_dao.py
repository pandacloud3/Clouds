from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.IntervalType import IntervalType


class IntervalTypeDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для типів інтервалів (Interval_type).
    """
    _domain_type = IntervalType

    def create(self, interval_type: IntervalType) -> None:
        """
        Додає новий тип інтервалу в базу даних.
        :param interval_type: об'єкт Interval_type, який потрібно додати
        """
        self._session.add(interval_type)
        self._session.commit()

    def find_all(self) -> List[IntervalType]:
        """
        Отримує всі типи інтервалів з таблиці бази даних.
        :return: список усіх типів інтервалів
        """
        return self._session.query(IntervalType).all()

    def find_by_name(self, name: str) -> List[IntervalType]:
        """
        Отримує типи інтервалів за назвою.
        :param name: назва інтервалу
        :return: список знайдених типів інтервалів
        """
        return self._session.query(IntervalType).filter(IntervalType.name == name).order_by(IntervalType.name).all()

    def find_by_id(self, interval_type_id: int) -> IntervalType:
        """
        Отримує тип інтервалу за його ID.
        :param interval_type_id: ID інтервалу
        :return: об'єкт Interval_type
        """
        return self._session.query(IntervalType).filter(IntervalType.id == interval_type_id).first()
