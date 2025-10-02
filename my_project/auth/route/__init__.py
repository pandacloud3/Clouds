"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)


    from .orders.data_route import data_bp
    from .orders.employee_route import employee_bp
    from .orders.employee_work_route import employee_work_bp
    from .orders.gender_route import gender_bp
    from .orders.interval_type_route import interval_type_bp
    from .orders.location_route import location_bp
    from .orders.message_of_data_route import message_of_data_bp
    from .orders.meteostation_route import meteostation_bp
    from .orders.meteostation_location_route import meteostation_location_bp
    from .orders.producer_route import producer_bp
    from .orders.service_work_route import service_work_bp
    from .orders.type_work_route import type_work_bp


    app.register_blueprint(meteostation_bp)
    app.register_blueprint(meteostation_location_bp)
    app.register_blueprint(data_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(employee_work_bp)
    app.register_blueprint(gender_bp)
    app.register_blueprint(interval_type_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(message_of_data_bp)
    app.register_blueprint(producer_bp)
    app.register_blueprint(service_work_bp)
    app.register_blueprint(type_work_bp)