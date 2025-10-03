from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import meteostation_controller
from my_project.auth.domain.orders.Meteostation import Meteostation

meteostation_bp = Blueprint('meteostations', __name__, url_prefix='/meteostations')


@meteostation_bp.get('')
def get_all_meteostations() -> Response:
    """
    Get all meteostations
    ---
    tags:
      - Meteostations
    parameters:
      - name: page
        in: query
        type: integer
        required: false
        default: 1
        description: The page number
    responses:
      200:
        description: A list of meteostations
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              location_id:
                type: integer
              producer_id:
                type: integer
              installation_date:
                type: string
              interval_id:
                type: integer
    """
    stations = meteostation_controller.find_all()
    stations_dto = [station.put_into_dto() for station in stations]
    return make_response(jsonify(stations_dto), HTTPStatus.OK)


@meteostation_bp.post('')
def create_meteostation() -> Response:
    """
    Create a new meteostation
    ---
    tags:
      - Meteostations
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            location_id:
              type: integer
            producer_id:
              type: integer
            installation_date:
              type: string
              format: date
            interval_id:
              type: integer
    responses:
      201:
        description: Meteostation created
    """

    content = request.get_json()
    station = Meteostation.create_from_dto(content)
    meteostation_controller.create(station)
    return make_response(jsonify(station.put_into_dto()), HTTPStatus.CREATED)


@meteostation_bp.get('/<int:station_id>')
def get_meteostation(station_id: int) -> Response:
    """
    Get a meteostation by ID
    ---
    tags:
      - Meteostations
    parameters:
      - name: station_id
        in: path
        type: integer
        required: true
        description: ID of the meteostation
    responses:
      200:
        description: Meteostation found
      404:
        description: Meteostation not found
    """
    station = meteostation_controller.find_by_id(station_id)
    if station:
        return make_response(jsonify(station.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Meteostation not found"}), HTTPStatus.NOT_FOUND)


@meteostation_bp.put('/<int:station_id>')
def update_meteostation(station_id: int) -> Response:
    """
    Update a meteostation by ID
    ---
    tags:
      - Meteostations
    parameters:
      - name: station_id
        in: path
        type: integer
        required: true
        description: ID of the meteostation
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: Meteostation updated
    """
    content = request.get_json()
    station = Meteostation.create_from_dto(content)
    meteostation_controller.update(station_id, station)
    return make_response("Meteostation updated", HTTPStatus.OK)


@meteostation_bp.delete('/<int:station_id>')
def delete_meteostation(station_id: int) -> Response:
    """
    Delete a meteostation by ID
    ---
    tags:
      - Meteostations
    parameters:
      - name: station_id
        in: path
        type: integer
        required: true
        description: ID of the meteostation
    responses:
      204:
        description: Meteostation deleted
    """
    meteostation_controller.delete(station_id)
    return make_response("Meteostation deleted", HTTPStatus.NO_CONTENT)


@meteostation_bp.get('/name/<string:name>')
def get_meteostations_by_name(name: str) -> Response:
    """
    Get meteostations by name
    ---
    tags:
      - Meteostations
    parameters:
      - name: name
        in: pat
        type: string
        required: true
        description: Meteostation name
    responses:
      200:
        description: List of meteostations with the given name
    """
    stations = meteostation_controller.get_stations_by_name(name)
    return make_response(jsonify([station.put_into_dto() for station in stations]), HTTPStatus.OK)


@meteostation_bp.get('/producer/<int:producer_id>')
def get_meteostations_by_producer(producer_id: int) -> Response:
    """
    Get meteostations by producer ID
    ---
    tags:
      - Meteostations
    parameters:
      - name: producer_id
        in: path
        type: integer
        required: true
        description: Producer ID
    responses:
      200:
        description: List of meteostations for the producer
    """
    stations = meteostation_controller.get_stations_by_producer(producer_id)
    return make_response(jsonify([station.put_into_dto() for station in stations]), HTTPStatus.OK)


@meteostation_bp.get('/interval/<int:interval_id>')
def get_meteostations_by_interval(interval_id: int) -> Response:
    """
    Get meteostations by interval ID
    ---
    tags:
      - Meteostations
    parameters:
      - name: interval_id
        in: path
        type: integer
        required: true
        description: Interval type ID
    responses:
      200:
        description: List of meteostations with given interval
    """
    stations = meteostation_controller.get_stations_by_interval(interval_id)
    return make_response(jsonify([station.put_into_dto() for station in stations]), HTTPStatus.OK)
