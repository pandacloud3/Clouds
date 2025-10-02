from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import interval_type_controller
from my_project.auth.domain.orders.IntervalType import IntervalType

interval_type_bp = Blueprint('interval_types', __name__, url_prefix='/interval_types')


@interval_type_bp.get('')
def get_all_interval_types() -> Response:
    """
    Gets all interval types from the database.
    :return: Response object
    """
    intervals = interval_type_controller.find_all()
    intervals_dto = [interval.put_into_dto() for interval in intervals]
    return make_response(jsonify(intervals_dto), HTTPStatus.OK)


@interval_type_bp.post('')
def create_interval_type() -> Response:
    """
    Creates a new interval type in the database.
    :return: Response object
    """
    content = request.get_json()
    interval = IntervalType.create_from_dto(content)
    interval_type_controller.create(interval)
    return make_response(jsonify(interval.put_into_dto()), HTTPStatus.CREATED)


@interval_type_bp.get('/<int:interval_id>')
def get_interval_type(interval_id: int) -> Response:
    """
    Gets interval type by ID.
    :param interval_id: ID of the interval type
    :return: Response object
    """
    interval = interval_type_controller.find_by_id(interval_id)
    if interval:
        return make_response(jsonify(interval.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Interval type not found"}), HTTPStatus.NOT_FOUND)


@interval_type_bp.put('/<int:interval_id>')
def update_interval_type(interval_id: int) -> Response:
    """
    Updates interval type by ID.
    :param interval_id: ID of the interval type
    :return: Response object
    """
    content = request.get_json()
    interval = IntervalType.create_from_dto(content)
    interval_type_controller.update(interval_id, interval)
    return make_response("Interval type updated", HTTPStatus.OK)


@interval_type_bp.delete('/<int:interval_id>')
def delete_interval_type(interval_id: int) -> Response:
    """
    Deletes interval type by ID.
    :param interval_id: ID of the interval type
    :return: Response object
    """
    interval_type_controller.delete(interval_id)
    return make_response("Interval type deleted", HTTPStatus.NO_CONTENT)


@interval_type_bp.get('/type/<string:type>')
def get_interval_types_by_type(type: str) -> Response:
    """
    Gets interval types by type name.
    :param type: Interval type string value
    :return: Response object
    """
    intervals = interval_type_controller.get_intervals_by_type(type)
    return make_response(jsonify([interval.put_into_dto() for interval in intervals]), HTTPStatus.OK)
