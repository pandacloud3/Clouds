from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.ServiceWork import ServiceWork


class ServiceWorkDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для сервісних робіт (ServiceWork).
    """
    _domain_type = ServiceWork

    def create(self, work: ServiceWork) -> None:
        """
        Додає нову сервісну роботу в базу даних.
        :param work: об'єкт ServiceWork, який потрібно додати
        """
        self._session.add(work)
        self._session.commit()

    def find_all(self) -> List[ServiceWork]:
        """
        Отримує всі сервісні роботи з таблиці бази даних.
        :return: список усіх робіт
        """
        return self._session.query(ServiceWork).all()

    def find_by_date(self, date: str) -> List[ServiceWork]:
        """
        Отримує сервісні роботи за датою.
        :param date: дата сервісної роботи (у форматі YYYY-MM-DD)
        :return: список знайдених робіт
        """
        return self._session.query(ServiceWork).filter(ServiceWork.date == date).order_by(ServiceWork.date).all()

    def find_by_meteostation(self, meteostation_id: int) -> List[ServiceWork]:
        """
        Отримує всі роботи для певної метеостанції.
        :param meteostation_id: ID метеостанції
        :return: список робіт
        """
        return self._session.query(ServiceWork).filter(ServiceWork.meteostation_id == meteostation_id).all()

    def find_by_type(self, type_work_id: int) -> List[ServiceWork]:
        """
        Отримує всі роботи певного типу.
        :param type_work_id: ID типу роботи
        :return: список робіт
        """
        return self._session.query(ServiceWork).filter(ServiceWork.type_work_id == type_work_id).all()

    def find_by_id(self, work_id: int) -> ServiceWork:
        """
        Отримує сервісну роботу за її ID.
        :param work_id: ID роботи
        :return: об'єкт ServiceWork
        """
        return self._session.query(ServiceWork).filter(ServiceWork.id == work_id).first()
