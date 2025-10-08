# import pymysql
# pymysql.install_as_MySQLdb()             /////////////////////

import os
from waitress import serve
import yaml
from flask import Flask
from my_project import create_app
from my_project.auth.controller.general_controller import general_controller
# from my_project.auth.service.general_service import insert_data
# from my_project.auth.controller.general_controller import animator_controller
# from my_project.auth.controller.general_controller import noname_animator_controller
# from my_project.auth.controller.general_controller import mmas_controller
# from my_project.auth.controller.general_controller import animator_distribute_controller


# DEVELOPMENT_PORT = 5000
# PRODUCTION_PORT = 8080
# HOST = "0.0.0.0"
# DEVELOPMENT = "development"
# PRODUCTION = "production"                           /////////
# FLASK_ENV = "FLASK_ENV"
# ADDITIONAL_CONFIG = "ADDITIONAL_CONFIG"


# def register_blueprints(app):
#     app.register_blueprint(general_controller)
#     app.register_blueprint(animator_controller)
#     app.register_blueprint(noname_animator_controller)
#     app.register_blueprint(mmas_controller)
#     app.register_blueprint(animator_distribute_controller)


# if __name__ == '__main__':                         //////////
#     app = create_app()
#     app.run(host="0.0.0.0", port=5000, debug=True)


    # flask_env = os.environ.get(FLASK_ENV, DEVELOPMENT).lower()
    # config_yaml_path = os.path.join(os.getcwd(), 'config', 'app.yml')
    #
    # with open(config_yaml_path, "r", encoding='utf-8') as yaml_file:
    #     config_data_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)
    #     additional_config = config_data_dict[ADDITIONAL_CONFIG]
    #
    #     if flask_env == DEVELOPMENT:
    #         config_data = config_data_dict[DEVELOPMENT]
    #         app = create_app(config_data, additional_config)
    #         # register_blueprints(app)
    #         app.run(host="0.0.0.0", port=DEVELOPMENT_PORT, debug=True)
    #
    #     elif flask_env == PRODUCTION:
    #         config_data = config_data_dict[PRODUCTION]
    #         app = create_app(config_data, additional_config)
    #         # register_blueprints(app)
    #         serve(app, host=HOST, port=PRODUCTION_PORT)
    #
    #     else:
    #         raise ValueError(f"Check OS environment variable '{FLASK_ENV}'")
from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from my_project.auth.route.orders.location_route import location_bp
from my_project.auth.route.auth_route import auth_bp

app = Flask(__name__)

# 🔐 JWT конфігурація
app.config["JWT_SECRET_KEY"] = "supersecretkey"  # зміни на власний секрет
jwt = JWTManager(app)

# 🔧 Swagger конфігурація з авторизацією
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

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

# 📦 Підключаємо Blueprint-и
app.register_blueprint(location_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
