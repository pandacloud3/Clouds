from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import location_controller
from my_project.auth.domain.orders.Location import Location
from my_project.extensions import basic_auth

location_bp = Blueprint('locations', __name__, url_prefix='/locations')


@location_bp.get('')
@basic_auth.required
def get_all_locations() -> Response:
    """
    Get all locations
    ---
    tags:
      - Locations
    responses:
      200:
        description: A list of all locations
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              location:
                type: string
              stat:
                type: string
    """
    locations_dto = location_controller.find_all()  # вже DTO
    return make_response(jsonify(locations_dto), HTTPStatus.OK)


@location_bp.post('')
def create_location() -> Response:
    """
    Create a new location
    ---
    tags:
      - Locations
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            location:
              type: string
            stat:
              type: string
    responses:
      201:
        description: Location created
    """
    content = request.get_json()
    loc = Location.create_from_dto(content)
    dto = location_controller.create(loc)
    return make_response(jsonify(dto), HTTPStatus.CREATED)


@location_bp.get('/<int:location_id>')
def get_location(location_id: int) -> Response:
    """
    Get a location by ID
    ---
    tags:
      - Locations
    parameters:
      - name: location_id
        in: path
        type: integer
        required: true
        description: ID of the location
    responses:
      200:
        description: Location found
      404:
        description: Location not found
    """
    loc = location_controller.find_by_id(location_id)
    if loc:
        return make_response(jsonify(loc.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Location not found"}), HTTPStatus.NOT_FOUND)


@location_bp.put('/<int:location_id>')
def update_location(location_id: int) -> Response:
    """
    Update a location by ID
    ---
    tags:
      - Locations
    parameters:
      - name: location_id
        in: path
        type: integer
        required: true
        description: ID of the location
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            location:
              type: string
            stat:
              type: string
    responses:
      200:
        description: Location updated
    """
    content = request.get_json()
    loc = Location.create_from_dto(content)
    location_controller.update(location_id, loc)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.delete('/<int:location_id>')
def delete_location(location_id: int) -> Response:
    """
    Delete a location by ID
    ---
    tags:
      - Locations
    parameters:
      - name: location_id
        in: path
        type: integer
        required: true
        description: ID of the location
    responses:
      204:
        description: Location deleted
    """
    location_controller.delete(location_id)
    return make_response("Location deleted", HTTPStatus.NO_CONTENT)


@location_bp.get('/name/<string:name>')
def get_locations_by_name(name: str) -> Response:
    """
    Get locations by name
    ---
    tags:
      - Locations
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: Location name
    responses:
      200:
        description: List of locations with the given name
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              location:
                type: string
              stat:
                type: string
    """
    locations = location_controller.find_by_name(name)
    return make_response(jsonify([loc.put_into_dto() for loc in locations]), HTTPStatus.OK)
