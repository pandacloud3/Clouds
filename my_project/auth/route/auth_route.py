from http import HTTPStatus
from flask_jwt_extended import create_access_token
from flask import Blueprint, request, Response, make_response, jsonify
from my_project.auth.domain.orders.Location import Location  # Використовуємо Location як модель

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.post("/login")
def login() -> Response:
    """
    Login
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
          required:
            - name
            - password
    responses:
      200:
        description: Login successful
        schema:
          type: object
          properties:
            access_token:
              type: string
              example: "<JWT token>"
      404:
        description: Invalid credentials
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Not found Location Lviv or bad password"
    """
    data = request.get_json()

    # Перевіряємо, що дані передані
    if not data or "name" not in data or "password" not in data:
        return make_response(jsonify({"message": "Name and password required"}), HTTPStatus.BAD_REQUEST)

    # Шукаємо Location по name
    loc = Location.query.filter_by(location=data["name"]).first()

    # Перевірка пароля
    if loc and getattr(loc, "password", None) == data["password"]:
        access_token = create_access_token(identity=str(loc.id))
        return make_response(jsonify({"access_token": access_token}), HTTPStatus.OK)

    return make_response(
        jsonify({"message": f"Not found Location {data.get('name')} or bad password"}),
        HTTPStatus.NOT_FOUND
    )
