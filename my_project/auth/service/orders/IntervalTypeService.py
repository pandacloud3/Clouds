from my_project.auth.dao import Interval_type_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.IntervalType import IntervalType


class IntervalTypeService(GeneralService):
    _dao = Interval_type_dao
