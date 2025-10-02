from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import location_controller
from my_project.auth.domain.orders.Location import Location

location_bp = Blueprint('locations', __name__, url_prefix='/locations')


@location_bp.get('')
def get_all_locations() -> Response:
    """
    Gets all locations from the database.
    :return: Response object
    """
    locations_dto = location_controller.find_all()  # вже DTO
    return make_response(jsonify(locations_dto), HTTPStatus.OK)


@location_bp.post('')
def create_location() -> Response:
    """
    Creates a new location in the database.
    :return: Response object
    """
    content = request.get_json()
    loc = Location.create_from_dto(content)
    dto = location_controller.create(loc)
    return make_response(jsonify(dto), HTTPStatus.CREATED)


@location_bp.get('/<int:location_id>')
def get_location(location_id: int) -> Response:
    """
    Gets location by ID.
    :param location_id: ID of the location
    :return: Response object
    """
    loc = location_controller.find_by_id(location_id)
    if loc:
        return make_response(jsonify(loc.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Location not found"}), HTTPStatus.NOT_FOUND)


@location_bp.put('/<int:location_id>')
def update_location(location_id: int) -> Response:
    """
    Updates location by ID.
    :param location_id: ID of the location
    :return: Response object
    """
    content = request.get_json()
    loc = Location.create_from_dto(content)
    location_controller.update(location_id, loc)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.delete('/<int:location_id>')
def delete_location(location_id: int) -> Response:
    """
    Deletes location by ID.
    :param location_id: ID of the location
    :return: Response object
    """
    location_controller.delete(location_id)
    return make_response("Location deleted", HTTPStatus.NO_CONTENT)


@location_bp.get('/name/<string:name>')
def get_locations_by_name(name: str) -> Response:
    """
    Gets locations by name.
    :param name: Location name
    :return: Response object
    """
    locations = location_controller.find_by_name(name)
    return make_response(jsonify([loc.put_into_dto() for loc in locations]), HTTPStatus.OK)
