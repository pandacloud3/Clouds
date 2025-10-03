"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from config import Config

import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flasgger import Swagger

from my_project.auth.route import register_routes
import pymysql
SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"
pymysql.install_as_MySQLdb()

# Database
db = SQLAlchemy()

todos = {}


def create_app() -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    :return: Flask application object
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    swagger = Swagger(app)

    _init_db(app)
    register_routes(app)


    return app





def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()

