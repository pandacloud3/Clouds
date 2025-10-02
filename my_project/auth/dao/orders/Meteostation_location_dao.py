from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.MeteostationLocation import MeteostationLocation


class MeteostationLocationDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для зв’язку між метеостанціями та локаціями (MeteostationLocation).
    """
    _domain_type = MeteostationLocation

    def create(self, link: MeteostationLocation) -> None:
        """
        Додає новий запис у зв’язок MeteostationLocation.
        :param link: об’єкт MeteostationLocation
        """
        self._session.add(link)
        self._session.commit()

    def find_all(self) -> List[MeteostationLocation]:
        """
        Отримує всі записи зв’язку між метеостанціями та локаціями.
        :return: список усіх зв’язків
        """
        return self._session.query(MeteostationLocation).all()

    def find_by_meteostation(self, meteostation_id: int) -> List[MeteostationLocation]:
        """
        Отримує всі записи зв’язку для певної метеостанції.
        :param meteostation_id: ID метеостанції
        :return: список зв’язків
        """
        return self._session.query(MeteostationLocation).filter(
            MeteostationLocation.meteostation_id == meteostation_id
        ).all()

    def find_by_location(self, location_id: int) -> List[MeteostationLocation]:
        """
        Отримує всі записи зв’язку для певної локації.
        :param location_id: ID локації
        :return: список зв’язків
        """
        return self._session.query(MeteostationLocation).filter(
            MeteostationLocation.location_id == location_id
        ).all()

    def find_pair(self, meteostation_id: int, location_id: int) -> MeteostationLocation:
        """
        Отримує конкретний запис зв’язку за парою (meteostation_id, location_id).
        :param meteostation_id: ID метеостанції
        :param location_id: ID локації
        :return: об’єкт MeteostationLocation або None
        """
        return (
            self._session.query(MeteostationLocation)
            .filter(
                MeteostationLocation.meteostation_id == meteostation_id,
                MeteostationLocation.location_id == location_id
            )
            .first()
        )
