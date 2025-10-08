from http import HTTPStatus
from flask_jwt_extended import create_access_token
from flask import Blueprint, request, Response, make_response, jsonify
from my_project.auth.domain.orders.Location import Location

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post("/login")
def login() -> Response:
    """
    Login to get JWT token
    ---
    tags:
      - Auth
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: "Lviv"
            password:
              type: string
              example: "password123"
    responses:
      200:
        description: Login successful
        schema:
          type: object
          properties:
            access_token:
              type: string
              example: "<access_token>"
      404:
        description: Invalid credentials
    """
    data = request.get_json()
    loc = Location.query.filter_by(name=data["name"]).first()

    if loc and getattr(loc, "password", None) == data["password"]:
        token = create_access_token(identity=str(loc.id))
        return make_response(jsonify({"access_token": token}), HTTPStatus.OK)
    return make_response(jsonify({"message": "Invalid name or password"}), HTTPStatus.NOT_FOUND)
