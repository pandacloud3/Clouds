from my_project.auth.dao import Service_work_dao
from my_project.auth.service.general_service import GeneralService
from my_project.auth.domain.orders.ServiceWork import ServiceWork


class ServiceWorkService(GeneralService):
    _dao = Service_work_dao
