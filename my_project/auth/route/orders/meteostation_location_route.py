from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import meteostation_location_controller
from my_project.auth.domain.orders.MeteostationLocation import MeteostationLocation

meteostation_location_bp = Blueprint('meteostation_locations', __name__, url_prefix='/meteostation_locations')


@meteostation_location_bp.get('')
def get_all_meteostation_locations() -> Response:
    """
    Gets all meteostation_location records from the database.
    :return: Response object
    """
    records = meteostation_location_controller.find_all()
    records_dto = [r.put_into_dto() for r in records]
    return make_response(jsonify(records_dto), HTTPStatus.OK)


@meteostation_location_bp.post('')
def create_meteostation_location() -> Response:
    """
    Creates a new meteostation_location record in the database.
    :return: Response object
    """
    content = request.get_json()
    record = MeteostationLocation.create_from_dto(content)
    meteostation_location_controller.create(record)
    return make_response(jsonify(record.put_into_dto()), HTTPStatus.CREATED)


@meteostation_location_bp.get('/<int:record_id>')
def get_meteostation_location(record_id: int) -> Response:
    """
    Gets meteostation_location record by ID.
    :param record_id: ID of the record
    :return: Response object
    """
    record = meteostation_location_controller.find_by_id(record_id)
    if record:
        return make_response(jsonify(record.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Record not found"}), HTTPStatus.NOT_FOUND)


@meteostation_location_bp.put('/<int:record_id>')
def update_meteostation_location(record_id: int) -> Response:
    """
    Updates meteostation_location record by ID.
    :param record_id: ID of the record
    :return: Response object
    """
    content = request.get_json()
    record = MeteostationLocation.create_from_dto(content)
    meteostation_location_controller.update(record_id, record)
    return make_response("Meteostation_location updated", HTTPStatus.OK)


@meteostation_location_bp.delete('/<int:record_id>')
def delete_meteostation_location(record_id: int) -> Response:
    """
    Deletes meteostation_location record by ID.
    :param record_id: ID of the record
    :return: Response object
    """
    meteostation_location_controller.delete(record_id)
    return make_response("Meteostation_location deleted", HTTPStatus.NO_CONTENT)


@meteostation_location_bp.get('/meteostation/<int:meteostation_id>')
def get_locations_by_meteostation(meteostation_id: int) -> Response:
    """
    Gets all location records associated with a specific meteostation.
    :param meteostation_id: Meteostation ID
    :return: Response object
    """
    records = meteostation_location_controller.find_by_meteostation_id(meteostation_id)
    return make_response(jsonify([r.put_into_dto() for r in records]), HTTPStatus.OK)


@meteostation_location_bp.get('/location/<int:location_id>')
def get_meteostations_by_location(location_id: int) -> Response:
    """
    Gets all meteostation records associated with a specific location.
    :param location_id: Location ID
    :return: Response object
    """
    records = meteostation_location_controller.find_by_location_id(location_id)
    return make_response(jsonify([r.put_into_dto() for r in records]), HTTPStatus.OK)
