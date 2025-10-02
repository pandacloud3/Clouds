from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Location import Location


class LocationDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для локацій (Location).
    """
    _domain_type = Location

    def create(self, location: Location) -> None:
        """
        Додає нову локацію в базу даних.
        :param location: об'єкт Location
        """
        self._session.add(location)
        self._session.commit()

    def find_all(self) -> List[Location]:
        """
        Отримує всі локації.
        :return: список усіх Location
        """
        return self._session.query(Location).all()

    def find_by_id(self, location_id: int) -> Location:
        """
        Отримує локацію за її ID.
        :param location_id: ID локації
        :return: об'єкт Location або None
        """
        return self._session.query(Location).filter(Location.id == location_id).first()

    def find_by_name(self, name: str) -> List[Location]:
        """
        Отримує всі локації з певною назвою.
        :param name: назва локації
        :return: список Location
        """
        return self._session.query(Location).filter(Location.location == name).order_by(Location.location).all()

    def find_by_stat(self, stat_value: str) -> List[Location]:
        """
        Отримує всі локації з певним статусом.
        :param stat_value: статус локації
        :return: список Location
        """
        return self._session.query(Location).filter(Location.stat == stat_value).order_by(Location.stat).all()
