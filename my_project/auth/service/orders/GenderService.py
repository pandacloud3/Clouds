from my_project.auth.dao import Gender_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Gender import Gender


class GenderService(GeneralService):
    _dao = Gender_dao
