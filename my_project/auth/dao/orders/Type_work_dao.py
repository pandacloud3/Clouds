from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.TypeWork import TypeWork


class TypeWorkDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для типів робіт (TypeWork).
    """
    _domain_type = TypeWork

    def create(self, type_work: TypeWork) -> None:
        """
        Додає новий тип роботи в базу даних.
        :param type_work: об'єкт TypeWork
        """
        self._session.add(type_work)
        self._session.commit()

    def find_all(self) -> List[TypeWork]:
        """
        Отримує всі типи робіт.
        :return: список усіх типів робіт
        """
        return self._session.query(TypeWork).all()

    def find_by_type(self, type_value: str) -> List[TypeWork]:
        """
        Отримує всі записи за значенням поля 'type'.
        :param type_value: назва типу роботи
        :return: список об'єктів TypeWork
        """
        return self._session.query(TypeWork).filter(TypeWork.type == type_value).order_by(TypeWork.type).all()

    def find_by_id(self, type_id: int) -> TypeWork:
        """
        Отримує тип роботи за його ID.
        :param type_id: ID типу роботи
        :return: об'єкт TypeWork
        """
        return self._session.query(TypeWork).filter(TypeWork.id == type_id).first()
