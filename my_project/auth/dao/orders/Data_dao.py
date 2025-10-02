from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Data import Data


class DataDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для метеорологічних даних (Data).
    """
    _domain_type = Data

    def create(self, data: Data) -> None:
        """
        Додає новий запис метеоданих у базу.
        :param data: об'єкт Data
        """
        self._session.add(data)
        self._session.commit()

    def find_all(self) -> List[Data]:
        """
        Отримує всі метеодані.
        :return: список Data
        """
        return self._session.query(Data).all()

    def find_by_id(self, data_id: int) -> Data:
        """
        Отримує запис метеоданих за ID.
        :param data_id: ID запису
        :return: об'єкт Data або None
        """
        return self._session.query(Data).filter(Data.id == data_id).first()

    def find_by_date(self, date: str) -> List[Data]:
        """
        Отримує всі записи за датою.
        :param date: дата (YYYY-MM-DD)
        :return: список Data
        """
        return self._session.query(Data).filter(Data.date == date).order_by(Data.date).all()

    def find_by_meteostation(self, meteostation_id: int) -> List[Data]:
        """
        Отримує всі записи для певної метеостанції.
        :param meteostation_id: ID метеостанції
        :return: список Data
        """
        return self._session.query(Data).filter(Data.meteostation_id == meteostation_id).all()

    def find_by_temperature_range(self, min_temp: float, max_temp: float) -> List[Data]:
        """
        Отримує всі записи з температурою в межах діапазону.
        :param min_temp: мінімальна температура
        :param max_temp: максимальна температура
        :return: список Data
        """
        return (self._session.query(Data)
                .filter(Data.temperature >= min_temp, Data.temperature <= max_temp)
                .all())
