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

    # SQLAlchemy
    db.init_app(app)

    # JWT
    JWTManager(app)

    # Swagger
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

    # Ініціалізація БД
    _init_db(app)

    # Міграції (опціонально)
    from flask_migrate import Migrate
    Migrate(app, db)

    # Реєстрація маршрутів
    register_routes(app)

    # Додаткові тригери / функції / процедури
    # create_triggers(app, db)
    # create_functions(app, db)
    # create_procedures(app, db)

    return app


def _init_db(app: Flask) -> None:
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']

    if not database_exists(database_uri):
        create_database(database_uri)

    import my_project.auth.domain

    with app.app_context():
        db.create_all()
