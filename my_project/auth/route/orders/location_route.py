from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import location_controller
from my_project.auth.domain.orders.Location import Location
from flask_jwt_extended import jwt_required

location_bp = Blueprint('location', __name__, url_prefix='/locations')


@location_bp.route('', methods=['GET'])
@jwt_required()
def get_all_locations() -> Response:
    """
    Get all Locations
    ---
    tags:
      - Location
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
    responses:
      200:
        description: List of all locations
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              location:
                type: string
                example: "Lviv"
              stat:
                type: string
                example: "active"
    """
    locations = location_controller.find_all()
    location_dto = [loc.put_into_dto() for loc in locations]
    return make_response(jsonify(location_dto), HTTPStatus.OK)


@location_bp.route('', methods=['POST'])
@jwt_required()
def create_location() -> Response:
    """
    Create a new Location
    ---
    tags:
      - Location
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - location
            - stat
          properties:
            location:
              type: string
              example: "Kyiv"
            stat:
              type: string
              example: "active"
    responses:
      201:
        description: Location created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 2
            location:
              type: string
              example: "Kyiv"
            stat:
              type: string
              example: "active"
    """
    content = request.get_json()
    loc = Location.create_from_dto(content)
    location_controller.create(loc)
    return make_response(jsonify(loc.put_into_dto()), HTTPStatus.CREATED)


@location_bp.route('/<int:location_id>', methods=['GET'])
@jwt_required()
def get_location_by_id(location_id: int) -> Response:
    """
    Get Location by ID
    ---
    tags:
      - Location
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
      - name: location_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Location found
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            location:
              type: string
              example: "Lviv"
            stat:
              type: string
              example: "active"
      404:
        description: Location not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Location not found"
    """
    loc = location_controller.find_by_id(location_id)
    if loc:
        return make_response(jsonify(loc.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Location not found"}), HTTPStatus.NOT_FOUND)


@location_bp.route('/<int:location_id>', methods=['PUT'])
@jwt_required()
def update_location(location_id: int) -> Response:
    """
    Update Location by ID
    ---
    tags:
      - Location
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
      - name: location_id
        in: path
        required: true
        type: integer
        example: 1
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - location
            - stat
          properties:
            location:
              type: string
              example: "Kharkiv"
            stat:
              type: string
              example: "inactive"
    responses:
      200:
        description: Location updated successfully
        schema:
          type: string
          example: "Location updated"
    """
    content = request.get_json()
    loc = Location.create_from_dto(content)
    location_controller.update(location_id, loc)
    return make_response("Location updated", HTTPStatus.OK)


@location_bp.route('/<int:location_id>', methods=['DELETE'])
@jwt_required()
def delete_location(location_id: int) -> Response:
    """
    Delete Location by ID
    ---
    tags:
      - Location
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
      - name: location_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      204:
        description: Location deleted successfully
        schema:
          type: string
          example: "Location deleted"
    """
    location_controller.delete(location_id)
    return make_response("Location deleted", HTTPStatus.NO_CONTENT)


@location_bp.route('/name/<string:name>', methods=['GET'])
@jwt_required()
def get_location_by_name(name: str) -> Response:
    """
    Get Locations by name
    ---
    tags:
      - Location
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
      - name: name
        in: path
        required: true
        type: string
        example: "Lviv"
    responses:
      200:
        description: List of locations found by name
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              location:
                type: string
                example: "Lviv"
              stat:
                type: string
                example: "active"
    """
    locations = location_controller.find_by_name(name)
    location_dto = [loc.put_into_dto() for loc in locations]
    return make_response(jsonify(location_dto), HTTPStatus.OK)
