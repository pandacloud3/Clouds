from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.MessageOfData import MessageOfData


class MessageOfDataDAO(GeneralDAO):
    """
    Реалізація рівня доступу даних для повідомлень з метеоданими (MessageOfData).
    """
    _domain_type = MessageOfData

    def create(self, message: MessageOfData) -> None:
        """
        Додає новий запис у MessageOfData.
        :param message: об'єкт MessageOfData
        """
        self._session.add(message)
        self._session.commit()

    def find_all(self) -> List[MessageOfData]:
        """
        Отримує всі записи з MessageOfData.
        :return: список усіх записів
        """
        return self._session.query(MessageOfData).all()

    def find_by_id(self, message_id: int) -> MessageOfData:
        """
        Отримує запис MessageOfData за ID.
        :param message_id: ID запису
        :return: об'єкт MessageOfData або None
        """
        return self._session.query(MessageOfData).filter(MessageOfData.id == message_id).first()

    def find_by_date(self, date: str) -> List[MessageOfData]:
        """
        Отримує всі повідомлення за датою.
        :param date: дата (YYYY-MM-DD)
        :return: список MessageOfData
        """
        return self._session.query(MessageOfData).filter(MessageOfData.date == date).order_by(MessageOfData.time).all()

    def find_by_meteostation(self, meteostation_id: int) -> List[MessageOfData]:
        """
        Отримує всі повідомлення для певної метеостанції.
        :param meteostation_id: ID метеостанції
        :return: список MessageOfData
        """
        return self._session.query(MessageOfData).filter(MessageOfData.meteostation_id == meteostation_id).all()

    def find_by_data(self, data_id: int) -> List[MessageOfData]:
        """
        Отримує всі повідомлення для певного запису метеоданих.
        :param data_id: ID метеоданих
        :return: список MessageOfData
        """
        return self._session.query(MessageOfData).filter(MessageOfData.data_id == data_id).all()
