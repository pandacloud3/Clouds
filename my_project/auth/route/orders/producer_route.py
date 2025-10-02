from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import producer_controller
from my_project.auth.domain.orders.Producer import Producer

producer_bp = Blueprint('producers', __name__, url_prefix='/producers')


@producer_bp.get('')
def get_all_producers() -> Response:
    """
    Gets all producers from the database.
    :return: Response object
    """
    producers = producer_controller.find_all()
    producers_dto = [producer.put_into_dto() for producer in producers]
    return make_response(jsonify(producers_dto), HTTPStatus.OK)


@producer_bp.post('')
def create_producer() -> Response:
    """
    Creates a new producer in the database.
    :return: Response object
    """
    content = request.get_json()
    producer = Producer.create_from_dto(content)
    producer_controller.create(producer)
    return make_response(jsonify(producer.put_into_dto()), HTTPStatus.CREATED)


@producer_bp.get('/<int:producer_id>')
def get_producer(producer_id: int) -> Response:
    """
    Gets producer by ID.
    :param producer_id: ID of the producer
    :return: Response object
    """
    producer = producer_controller.find_by_id(producer_id)
    if producer:
        return make_response(jsonify(producer.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Producer not found"}), HTTPStatus.NOT_FOUND)


@producer_bp.put('/<int:producer_id>')
def update_producer(producer_id: int) -> Response:
    """
    Updates producer by ID.
    :param producer_id: ID of the producer
    :return: Response object
    """
    content = request.get_json()
    producer = Producer.create_from_dto(content)
    producer_controller.update(producer_id, producer)
    return make_response("Producer updated", HTTPStatus.OK)


@producer_bp.delete('/<int:producer_id>')
def delete_producer(producer_id: int) -> Response:
    """
    Deletes producer by ID.
    :param producer_id: ID of the producer
    :return: Response object
    """
    producer_controller.delete(producer_id)
    return make_response("Producer deleted", HTTPStatus.NO_CONTENT)


@producer_bp.get('/name/<string:name>')
def get_producers_by_name(name: str) -> Response:
    """
    Gets producers by name.
    :param name: Producer name
    :return: Response object
    """
    producers = producer_controller.get_producers_by_name(name)
    return make_response(jsonify([producer.put_into_dto() for producer in producers]), HTTPStatus.OK)


@producer_bp.get('/address/<string:address>')
def get_producers_by_address(address: str) -> Response:
    """
    Gets producers by address.
    :param address: Producer address
    :return: Response object
    """
    producers = producer_controller.get_producers_by_address(address)
    return make_response(jsonify([producer.put_into_dto() for producer in producers]), HTTPStatus.OK)
