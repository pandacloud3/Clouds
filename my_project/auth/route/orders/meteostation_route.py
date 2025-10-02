from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import meteostation_controller
from my_project.auth.domain.orders.Meteostation import Meteostation

meteostation_bp = Blueprint('meteostations', __name__, url_prefix='/meteostations')


@meteostation_bp.get('')
def get_all_meteostations() -> Response:
    """
    Gets all meteostations from the database.
    :return: Response object
    """
    stations = meteostation_controller.find_all()
    stations_dto = [station.put_into_dto() for station in stations]
    return make_response(jsonify(stations_dto), HTTPStatus.OK)


@meteostation_bp.post('')
def create_meteostation() -> Response:
    """
    Creates a new meteostation in the database.
    :return: Response object
    """
    content = request.get_json()
    station = Meteostation.create_from_dto(content)
    meteostation_controller.create(station)
    return make_response(jsonify(station.put_into_dto()), HTTPStatus.CREATED)


@meteostation_bp.get('/<int:station_id>')
def get_meteostation(station_id: int) -> Response:
    """
    Gets meteostation by ID.
    :param station_id: ID of the meteostation
    :return: Response object
    """
    station = meteostation_controller.find_by_id(station_id)
    if station:
        return make_response(jsonify(station.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Meteostation not found"}), HTTPStatus.NOT_FOUND)


@meteostation_bp.put('/<int:station_id>')
def update_meteostation(station_id: int) -> Response:
    """
    Updates meteostation by ID.
    :param station_id: ID of the meteostation
    :return: Response object
    """
    content = request.get_json()
    station = Meteostation.create_from_dto(content)
    meteostation_controller.update(station_id, station)
    return make_response("Meteostation updated", HTTPStatus.OK)


@meteostation_bp.delete('/<int:station_id>')
def delete_meteostation(station_id: int) -> Response:
    """
    Deletes meteostation by ID.
    :param station_id: ID of the meteostation
    :return: Response object
    """
    meteostation_controller.delete(station_id)
    return make_response("Meteostation deleted", HTTPStatus.NO_CONTENT)


@meteostation_bp.get('/name/<string:name>')
def get_meteostations_by_name(name: str) -> Response:
    """
    Gets meteostations by name.
    :param name: Meteostation name
    :return: Response object
    """
    stations = meteostation_controller.get_stations_by_name(name)
    return make_response(jsonify([station.put_into_dto() for station in stations]), HTTPStatus.OK)


@meteostation_bp.get('/producer/<int:producer_id>')
def get_meteostations_by_producer(producer_id: int) -> Response:
    """
    Gets meteostations by producer ID.
    :param producer_id: Producer ID
    :return: Response object
    """
    stations = meteostation_controller.get_stations_by_producer(producer_id)
    return make_response(jsonify([station.put_into_dto() for station in stations]), HTTPStatus.OK)


@meteostation_bp.get('/interval/<int:interval_id>')
def get_meteostations_by_interval(interval_id: int) -> Response:
    """
    Gets meteostations by interval ID.
    :param interval_id: Interval type ID
    :return: Response object
    """
    stations = meteostation_controller.get_stations_by_interval(interval_id)
    return make_response(jsonify([station.put_into_dto() for station in stations]), HTTPStatus.OK)
