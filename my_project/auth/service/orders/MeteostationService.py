from my_project.auth.dao import meteostationdao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Meteostation import Meteostation


class MeteostationService(GeneralService):
    _dao = meteostationdao
