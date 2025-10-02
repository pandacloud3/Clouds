from my_project.auth.dao import Type_work_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.TypeWork import TypeWork


class TypeWorkService(GeneralService):
    _dao = Type_work_dao
