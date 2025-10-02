from my_project.auth.dao import Location_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.Location import Location


class LocationService(GeneralService):
    _dao = Location_dao
