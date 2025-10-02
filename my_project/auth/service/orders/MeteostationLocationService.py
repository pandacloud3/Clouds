from my_project.auth.dao import Meteostation_location_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.MeteostationLocation import MeteostationLocation


class MeteostationLocationService(GeneralService):
    _dao = Meteostation_location_dao
