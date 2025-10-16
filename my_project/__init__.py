"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

import pymysql
from flasgger import Swagger
from config import Config
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from my_project.auth.route import register_routes

# # Константи (якщо не задаються у Config)
# SECRET_KEY = "SECRET_KEY"
# SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
# MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
# MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

# Database
db = SQLAlchemy()
pymysql.install_as_MySQLdb()

todos = {}


def create_app() -> Flask:
    """
    Створює Flask-застосунок,
    підключає Swagger, JWT та базу даних.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # Ініціалізація JWT
    jwt = JWTManager(app)

    # Swagger для документації
    swagger = Swagger(app)

    # Ініціалізація бази даних
    _init_db(app)

    from flask_migrate import Migrate

    # Після ініціалізації бази
    migrate = Migrate(app, db)

    # Реєстрація маршрутів
    register_routes(app)

    return app


# def _init_db(app: Flask) -> None:
#     """
#     Ініціалізація бази даних через SQLAlchemy.
#     Якщо БД ще не створена — створює її.
#     """
#     db.init_app(app)
#
#     if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
#         create_database(app.config[SQLALCHEMY_DATABASE_URI])
#
#     import my_project.auth.domain
#     with app.app_context():
#         db.create_all()

def _init_db(app: Flask) -> None:
    """
    Ініціалізація бази даних через SQLAlchemy.
    Якщо БД ще не створена — створює її.
    """
    db.init_app(app)

    from sqlalchemy_utils import database_exists, create_database

    # Правильний ключ для доступу до URI
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']

    # Створюємо базу, якщо не існує
    if not database_exists(database_uri):
        create_database(database_uri)

    # Імпорт моделей
    import my_project.auth.domain

    # Створюємо таблиці
    with app.app_context():
        db.create_all()
