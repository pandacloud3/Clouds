from my_project.auth.dao import Data_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Meteostation import Meteostation


class DataService(GeneralService):
    _dao = Data_dao
