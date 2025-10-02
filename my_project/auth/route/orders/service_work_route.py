from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import service_work_controller
from my_project.auth.domain.orders.ServiceWork import ServiceWork

service_work_bp = Blueprint('service_works', __name__, url_prefix='/service_works')


@service_work_bp.get('')
def get_all_service_works() -> Response:
    """
    Gets all service works from the database.
    :return: Response object
    """
    works = service_work_controller.find_all()
    works_dto = [work.put_into_dto() for work in works]
    return make_response(jsonify(works_dto), HTTPStatus.OK)


@service_work_bp.post('')
def create_service_work() -> Response:
    """
    Creates a new service work in the database.
    :return: Response object
    """
    content = request.get_json()
    work = ServiceWork.create_from_dto(content)
    service_work_controller.create(work)
    return make_response(jsonify(work.put_into_dto()), HTTPStatus.CREATED)


@service_work_bp.get('/<int:work_id>')
def get_service_work(work_id: int) -> Response:
    """
    Gets service work by ID.
    :param work_id: ID of the service work
    :return: Response object
    """
    work = service_work_controller.find_by_id(work_id)
    if work:
        return make_response(jsonify(work.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Service work not found"}), HTTPStatus.NOT_FOUND)


@service_work_bp.put('/<int:work_id>')
def update_service_work(work_id: int) -> Response:
    """
    Updates service work by ID.
    :param work_id: ID of the service work
    :return: Response object
    """
    content = request.get_json()
    work = ServiceWork.create_from_dto(content)
    service_work_controller.update(work_id, work)
    return make_response("Service work updated", HTTPStatus.OK)


@service_work_bp.delete('/<int:work_id>')
def delete_service_work(work_id: int) -> Response:
    """
    Deletes service work by ID.
    :param work_id: ID of the service work
    :return: Response object
    """
    service_work_controller.delete(work_id)
    return make_response("Service work deleted", HTTPStatus.NO_CONTENT)


@service_work_bp.get('/meteostation/<int:meteostation_id>')
def get_service_works_by_meteostation(meteostation_id: int) -> Response:
    """
    Gets all service works for a specific meteostation.
    :param meteostation_id: ID of the meteostation
    :return: Response object
    """
    works = service_work_controller.get_service_works_by_meteostation(meteostation_id)
    return make_response(jsonify([work.put_into_dto() for work in works]), HTTPStatus.OK)


@service_work_bp.get('/type_work/<int:type_work_id>')
def get_service_works_by_type(type_work_id: int) -> Response:
    """
    Gets all service works by type of work.
    :param type_work_id: ID of the type of work
    :return: Response object
    """
    works = service_work_controller.get_service_works_by_type(type_work_id)
    return make_response(jsonify([work.put_into_dto() for work in works]), HTTPStatus.OK)
