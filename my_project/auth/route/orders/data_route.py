from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import data_controller
from my_project.auth.domain.orders.Data import Data

data_bp = Blueprint('data', __name__, url_prefix='/data')


@data_bp.get('')
def get_all_data() -> Response:
    """
    Gets all data records from the database.
    :return: Response object
    """
    records = data_controller.find_all()
    records_dto = [record.put_into_dto() for record in records]
    return make_response(jsonify(records_dto), HTTPStatus.OK)


@data_bp.post('')
def create_data() -> Response:
    """
    Creates a new data record in the database.
    :return: Response object
    """
    content = request.get_json()
    record = Data.create_from_dto(content)
    data_controller.create(record)
    return make_response(jsonify(record.put_into_dto()), HTTPStatus.CREATED)


@data_bp.get('/<int:data_id>')
def get_data(data_id: int) -> Response:
    """
    Gets data record by ID.
    :param data_id: ID of the data record
    :return: Response object
    """
    record = data_controller.find_by_id(data_id)
    if record:
        return make_response(jsonify(record.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Data not found"}), HTTPStatus.NOT_FOUND)


@data_bp.put('/<int:data_id>')
def update_data(data_id: int) -> Response:
    """
    Updates data record by ID.
    :param data_id: ID of the data record
    :return: Response object
    """
    content = request.get_json()
    record = Data.create_from_dto(content)
    data_controller.update(data_id, record)
    return make_response("Data record updated", HTTPStatus.OK)


@data_bp.delete('/<int:data_id>')
def delete_data(data_id: int) -> Response:
    """
    Deletes data record by ID.
    :param data_id: ID of the data record
    :return: Response object
    """
    data_controller.delete(data_id)
    return make_response("Data record deleted", HTTPStatus.NO_CONTENT)


@data_bp.get('/meteostation/<int:meteostation_id>')
def get_data_by_meteostation(meteostation_id: int) -> Response:
    """
    Gets all data records for a specific meteostation.
    :param meteostation_id: Meteostation ID
    :return: Response object
    """
    records = data_controller.find_by_meteostation_id(meteostation_id)
    return make_response(jsonify([record.put_into_dto() for record in records]), HTTPStatus.OK)


@data_bp.get('/date/<string:date>')
def get_data_by_date(date: str) -> Response:
    """
    Gets all data records for a specific date.
    :param date: Date string (YYYY-MM-DD)
    :return: Response object
    """
    records = data_controller.find_by_date(date)
    return make_response(jsonify([record.put_into_dto() for record in records]), HTTPStatus.OK)
