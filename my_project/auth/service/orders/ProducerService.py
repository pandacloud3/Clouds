from typing import List
from my_project.auth.dao import Producer_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Producer import Producer


class ProducerService(GeneralService):
    _dao = Producer_dao

