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

# 🔧 Database
db = SQLAlchemy()
pymysql.install_as_MySQLdb()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # 1️⃣ SQLAlchemy
    db.init_app(app)

    # 2️⃣ JWT
    JWTManager(app)

    # 3️⃣ Swagger
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
        # Глобально для всіх маршрутів
        "security": [{"Bearer": []}]
    }
    Swagger(app, template=swagger_template)

    # 4️⃣ Ініціалізація БД
    _init_db(app)

    # # 5️⃣ Міграції (опціонально)
    # from flask_migrate import Migrate
    # Migrate(app, db)

    # 6️⃣ Реєстрація маршрутів
    register_routes(app)

    # 7️⃣ Додаткові тригери / функції / процедури (якщо потрібно)
    # create_triggers(app, db)
    # create_functions(app, db)
    # create_procedures(app, db)

    return app


def _init_db(app: Flask) -> None:
    """
    Ініціалізація бази даних через SQLAlchemy.
    Якщо БД ще не створена — створює її.
    """
    database_uri = app.config['SQLALCHEMY_DATABASE_URI']

    # Створюємо базу, якщо не існує
    if not database_exists(database_uri):
        create_database(database_uri)

    # Імпорт моделей
    import my_project.auth.domain  # тут твої моделі

    # Створюємо таблиці
    with app.app_context():
        db.create_all()
