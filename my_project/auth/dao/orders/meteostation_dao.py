from typing import List, Optional
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Meteostation import Meteostation


class MeteostationDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для метеостанцій.
    """
    _domain_type = Meteostation

    def create(self, station: Meteostation) -> None:
        """
        Додає нову метеостанцію в базу даних.
        :param station: метеостанція, яку потрібно додати
        """
        self._session.add(station)
        self._session.commit()

    def find_all(self) -> List[Meteostation]:
        """
        Отримує всі метеостанції з таблиці бази даних.
        :return: список всіх метеостанцій
        """
        return self._session.query(Meteostation).all()

    def find_by_name(self, name: str) -> List[Meteostation]:
        """
        Отримує метеостанції з таблиці бази даних за полем 'name'.
        :param name: значення назви
        :return: знайдені об'єкти
        """
        return (
            self._session.query(Meteostation)
            .filter(Meteostation.name == name)
            .order_by(Meteostation.name)
            .all()
        )

    def find_by_producer(self, producer_id: int) -> List[Meteostation]:
        """
        Отримує метеостанції з таблиці бази даних за producer_id.
        :param producer_id: ID виробника
        :return: знайдені об'єкти
        """
        return (
            self._session.query(Meteostation)
            .filter(Meteostation.producer_id == producer_id)
            .order_by(Meteostation.name)
            .all()
        )

    def find_by_interval(self, interval_id: int) -> List[Meteostation]:
        """
        Отримує метеостанції з таблиці бази даних за interval_id.
        :param interval_id: ID інтервалу
        :return: знайдені об'єкти
        """
        return (
            self._session.query(Meteostation)
            .filter(Meteostation.interval_id == interval_id)
            .all()
        )

    def find_by_id(self, station_id: int) -> Optional[Meteostation]:
        """
        Отримує метеостанцію за ID.
        :param station_id: ID метеостанції
        :return: метеостанція або None
        """
        return (
            self._session.query(Meteostation)
            .filter(Meteostation.id == station_id)
            .first()
        )
