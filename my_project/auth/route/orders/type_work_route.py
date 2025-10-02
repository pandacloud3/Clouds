from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import type_work_controller
from my_project.auth.domain.orders.TypeWork import TypeWork

type_work_bp = Blueprint('type_works', __name__, url_prefix='/type_works')


@type_work_bp.get('')
def get_all_type_works() -> Response:
    """
    Gets all types of work from the database.
    :return: Response object
    """
    works = type_work_controller.find_all()
    works_dto = [work.put_into_dto() for work in works]
    return make_response(jsonify(works_dto), HTTPStatus.OK)


@type_work_bp.post('')
def create_type_work() -> Response:
    """
    Creates a new type of work in the database.
    :return: Response object
    """
    content = request.get_json()
    work = TypeWork.create_from_dto(content)
    type_work_controller.create(work)
    return make_response(jsonify(work.put_into_dto()), HTTPStatus.CREATED)


@type_work_bp.get('/<int:work_id>')
def get_type_work(work_id: int) -> Response:
    """
    Gets type of work by ID.
    :param work_id: ID of the type of work
    :return: Response object
    """
    work = type_work_controller.find_by_id(work_id)
    if work:
        return make_response(jsonify(work.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Type of work not found"}), HTTPStatus.NOT_FOUND)


@type_work_bp.put('/<int:work_id>')
def update_type_work(work_id: int) -> Response:
    """
    Updates type of work by ID.
    :param work_id: ID of the type of work
    :return: Response object
    """
    content = request.get_json()
    work = TypeWork.create_from_dto(content)
    type_work_controller.update(work_id, work)
    return make_response("Type of work updated", HTTPStatus.OK)


@type_work_bp.delete('/<int:work_id>')
def delete_type_work(work_id: int) -> Response:
    """
    Deletes type of work by ID.
    :param work_id: ID of the type of work
    :return: Response object
    """
    type_work_controller.delete(work_id)
    return make_response("Type of work deleted", HTTPStatus.NO_CONTENT)


@type_work_bp.get('/by_name/<string:name>')
def get_type_work_by_name(name: str) -> Response:
    """
    Gets type of work by its name.
    :param name: Name of the type of work
    :return: Response object
    """
    work = type_work_controller.find_by_name(name)
    if work:
        return make_response(jsonify(work.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Type of work not found"}), HTTPStatus.NOT_FOUND)
