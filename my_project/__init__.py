"""
my_project/__init__.py
Повністю робочий init для Flask + SQLAlchemy + JWT + Swagger
"""

import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from config import Config
from my_project.auth.route import register_routes
# from my_project.additional_for_db.additional_for_db import create_triggers, create_procedures, create_functions

db = SQLAlchemy()
pymysql.install_as_MySQLdb()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    JWTManager(app)

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "A swagger API",
            "description": "API з JWT авторизацією",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header. Example: 'Bearer {token}'"
            }
        },
        "security": [{"Bearer": []}]
    }
    Swagger(app, template=swagger_template)

    _init_db(app)


    register_routes(app)

    return app


def _init_db(app: Flask) -> None:
    """
    Ініціалізація бази даних через SQLAlchemy.
    Якщо БД ще не створена — створює її.
    """
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']

    if not database_exists(database_uri):
        create_database(database_uri)


    import my_project.auth.domain 

    with app.app_context():
        db.create_all()
