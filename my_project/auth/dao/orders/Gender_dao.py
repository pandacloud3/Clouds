from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Gender import Gender


class GenderDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для гендерів (Gender).
    """
    _domain_type = Gender

    def create(self, gender: Gender) -> None:
        """
        Додає новий гендер у базу даних.
        :param gender: об'єкт Gender
        """
        self._session.add(gender)
        self._session.commit()

    def find_all(self) -> List[Gender]:
        """
        Отримує всі гендери.
        :return: список усіх Gender
        """
        return self._session.query(Gender).all()

    def find_by_id(self, gender_id: int) -> Gender:
        """
        Отримує гендер за його ID.
        :param gender_id: ID гендеру
        :return: об'єкт Gender або None
        """
        return self._session.query(Gender).filter(Gender.id == gender_id).first()

    def find_by_type(self, type_value: str) -> List[Gender]:
        """
        Отримує всі гендери за назвою.
        :param type_value: назва гендеру
        :return: список Gender
        """
        return self._session.query(Gender).filter(Gender.type == type_value).order_by(Gender.type).all()
