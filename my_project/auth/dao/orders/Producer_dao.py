from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Producer import Producer


class ProducerDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для виробників (producer).
    """
    _domain_type = Producer

    def create(self, producer: Producer) -> None:
        """
        Додає нового виробника в базу даних.
        :param producer: об'єкт Producer, який потрібно додати
        """
        self._session.add(producer)
        self._session.commit()

    def find_all(self) -> List[Producer]:
        """
        Отримує всіх виробників з таблиці бази даних.
        :return: список усіх виробників
        """
        return self._session.query(Producer).all()

    def find_by_name(self, name: str) -> List[Producer]:
        """
        Отримує виробників з таблиці бази даних за полем name.
        :param name: назва виробника
        :return: список знайдених виробників
        """
        return self._session.query(Producer).filter(Producer.name == name).order_by(Producer.name).all()

    def find_by_id(self, producer_id: int) -> Producer:
        """
        Отримує виробника за його ID.
        :param producer_id: ID виробника
        :return: об'єкт Producer
        """
        return self._session.query(Producer).filter(Producer.id == producer_id).first()
