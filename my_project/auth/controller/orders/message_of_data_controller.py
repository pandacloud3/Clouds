from my_project.auth.service import message_of_data_service
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.MessageOfData import MessageOfData


class MessageOfDataController(GeneralController):
    _service = message_of_data_service