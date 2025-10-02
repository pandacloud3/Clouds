from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import gender_controller
from my_project.auth.domain.orders.Gender import Gender

gender_bp = Blueprint('genders', __name__, url_prefix='/genders')


@gender_bp.get('')
def get_all_genders() -> Response:
    """
    Gets all genders from the database.
    :return: Response object
    """
    genders = gender_controller.find_all()
    genders_dto = [g.put_into_dto() for g in genders]
    return make_response(jsonify(genders_dto), HTTPStatus.OK)


@gender_bp.post('')
def create_gender() -> Response:
    """
    Creates a new gender in the database.
    :return: Response object
    """
    content = request.get_json()
    gender = Gender.create_from_dto(content)
    gender_controller.create(gender)
    return make_response(jsonify(gender.put_into_dto()), HTTPStatus.CREATED)


@gender_bp.get('/<int:gender_id>')
def get_gender(gender_id: int) -> Response:
    """
    Gets gender by ID.
    :param gender_id: ID of the gender
    :return: Response object
    """
    gender = gender_controller.find_by_id(gender_id)
    if gender:
        return make_response(jsonify(gender.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Gender not found"}), HTTPStatus.NOT_FOUND)


@gender_bp.put('/<int:gender_id>')
def update_gender(gender_id: int) -> Response:
    """
    Updates gender by ID.
    :param gender_id: ID of the gender
    :return: Response object
    """
    content = request.get_json()
    gender = Gender.create_from_dto(content)
    gender_controller.update(gender_id, gender)
    return make_response("Gender updated", HTTPStatus.OK)


@gender_bp.delete('/<int:gender_id>')
def delete_gender(gender_id: int) -> Response:
    """
    Deletes gender by ID.
    :param gender_id: ID of the gender
    :return: Response object
    """
    gender_controller.delete(gender_id)
    return make_response("Gender deleted", HTTPStatus.NO_CONTENT)


@gender_bp.get('/name/<string:name>')
def get_gender_by_name(name: str) -> Response:
    """
    Gets gender by name (e.g., Male, Female, Other).
    :param name: Gender name
    :return: Response object
    """
    genders = gender_controller.find_by_name(name)
    return make_response(jsonify([g.put_into_dto() for g in genders]), HTTPStatus.OK)
