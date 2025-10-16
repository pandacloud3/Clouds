"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from config import Config
from my_project.auth.route import register_routes

# Database
db = SQLAlchemy()
pymysql.install_as_MySQLdb()


def create_app() -> Flask:
    """
    Створює Flask-застосунок,
    підключає Swagger, JWT та базу даних.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    # 1️⃣ Ініціалізація SQLAlchemy
    db.init_app(app)

    # 2️⃣ Ініціалізація JWT
    JWTManager(app)

    # 3️⃣ Swagger для документації
    Swagger(app)

    # 4️⃣ Ініціалізація бази даних
    _init_db(app)

    

    # 6️⃣ Реєстрація маршрутів
    register_routes(app)

    # 7️⃣ Додаткові тригери, функції, процедури (розкоментуй якщо потрібно)
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
    import my_project.auth.domain

    # Створюємо таблиці в контексті додатку
    with app.app_context():
        db.create_all()
