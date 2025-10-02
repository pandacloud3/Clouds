from my_project.auth.dao import Message_of_data_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.MessageOfData import MessageOfData


class MessageOfDataService(GeneralService):
    _dao = Message_of_data_dao
