from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token
from http import HTTPStatus
from my_project.auth.domain.orders.Location import Location
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.post("/login")
@swag_from({
    "tags": ["Auth"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "example": "Lviv"},
                    "password": {"type": "string", "example": "password123"}
                },
                "required": ["location", "password"]
            }
        }
    ],
    "responses": {
        200: {
            "description": "Login successful",
            "schema": {
                "type": "object",
                "properties": {
                    "access_token": {"type": "string", "example": "<JWT token>"}
                }
            }
        },
        404: {"description": "Invalid credentials"}
    }
})
def login():
    data = request.get_json()
    loc = Location.query.filter_by(location=data["location"]).first()
    if loc and getattr(loc, "password", None) == data["password"]:
        token = create_access_token(identity=str(loc.id))
        return make_response(jsonify({"access_token": token}), HTTPStatus.OK)
    return make_response(jsonify({"message": "Invalid name or password"}), HTTPStatus.NOT_FOUND)
