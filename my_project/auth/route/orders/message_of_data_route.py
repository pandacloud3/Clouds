from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import message_of_data_controller
from my_project.auth.domain.orders.MessageOfData import MessageOfData

message_of_data_bp = Blueprint('message_of_data', __name__, url_prefix='/message_of_data')


@message_of_data_bp.get('')
def get_all_messages() -> Response:
    """
    Gets all message_of_data records from the database.
    :return: Response object
    """
    messages = message_of_data_controller.find_all()
    messages_dto = [msg.put_into_dto() for msg in messages]
    return make_response(jsonify(messages_dto), HTTPStatus.OK)


@message_of_data_bp.post('')
def create_message() -> Response:
    """
    Creates a new message_of_data record in the database.
    :return: Response object
    """
    content = request.get_json()
    msg = MessageOfData.create_from_dto(content)
    message_of_data_controller.create(msg)
    return make_response(jsonify(msg.put_into_dto()), HTTPStatus.CREATED)


@message_of_data_bp.get('/<int:message_id>')
def get_message(message_id: int) -> Response:
    """
    Gets message_of_data record by ID.
    :param message_id: ID of the message
    :return: Response object
    """
    msg = message_of_data_controller.find_by_id(message_id)
    if msg:
        return make_response(jsonify(msg.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Message not found"}), HTTPStatus.NOT_FOUND)


@message_of_data_bp.put('/<int:message_id>')
def update_message(message_id: int) -> Response:
    """
    Updates message_of_data record by ID.
    :param message_id: ID of the message
    :return: Response object
    """
    content = request.get_json()
    msg = MessageOfData.create_from_dto(content)
    message_of_data_controller.update(message_id, msg)
    return make_response("Message updated", HTTPStatus.OK)


@message_of_data_bp.delete('/<int:message_id>')
def delete_message(message_id: int) -> Response:
    """
    Deletes message_of_data record by ID.
    :param message_id: ID of the message
    :return: Response object
    """
    message_of_data_controller.delete(message_id)
    return make_response("Message deleted", HTTPStatus.NO_CONTENT)


@message_of_data_bp.get('/meteostation/<int:meteostation_id>')
def get_messages_by_meteostation(meteostation_id: int) -> Response:
    """
    Gets all message_of_data records for a specific meteostation.
    :param meteostation_id: Meteostation ID
    :return: Response object
    """
    messages = message_of_data_controller.find_by_meteostation_id(meteostation_id)
    return make_response(jsonify([msg.put_into_dto() for msg in messages]), HTTPStatus.OK)


@message_of_data_bp.get('/data/<int:data_id>')
def get_messages_by_data(data_id: int) -> Response:
    """
    Gets all message_of_data records for a specific data record.
    :param data_id: Data record ID
    :return: Response object
    """
    messages = message_of_data_controller.find_by_data_id(data_id)
    return make_response(jsonify([msg.put_into_dto() for msg in messages]), HTTPStatus.OK)
