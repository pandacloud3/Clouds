"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from abc import ABC
from typing import List, Dict

from http import HTTPStatus
from flask import abort, Blueprint, request, jsonify
# from my_project.auth.service.general_service import insert_data
# from my_project.auth.service.general_service import add_animator_to_agency
# from my_project.auth.service.general_service import insert_noname_animators
# from my_project.auth.service.general_service import get_column_stat
# from my_project.auth.service.general_service import distribute_animators_data


class GeneralController(ABC):
    """
    The common realization of controller.
    """
    _service = None

    def find_all(self) -> List[object]:
        """
        Gets all objects from table using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        # return list(map(lambda x: x.put_into_dto(), self._service.find_all()))
        return [x.put_into_dto() for x in self._service.find_all()]

    def find_by_id(self, key: int) -> object:
        """
        Gets object from database table by integer key using from Service layer.
        :param key: integer key (surrogate primary key)
        :return: DTO for search object
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.put_into_dto()

    def create(self, obj):
        self._service.create(obj)
        return obj.put_into_dto()  # повертаємо DTO, а не None

    def create_all(self, obj_list: List[object]) -> List[object]:
        """
        Creates objects from object list using Service layer.
        :param obj_list: object list to create in Database
        :return: list of created objects as DTOs
        """
        return list(map(lambda x: x.put_into_dto(), self._service.create(obj_list)))

    def update(self, key: int, new_obj: object) -> None:
        """
        Updates object in database table using Service layer.
        :param key: integer key (surrogate primary key)
        :param new_obj: object to create in Database
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(key, new_obj)

    def patch(self, key: int, value_dict: Dict[str, object]) -> None:
        """
        Modifies defined field of object in database table using Service layer.
        :param key: integer key (surrogate primary key)
        :param value_dict: key-values
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        for field_name, value in value_dict.items():
            self._service.patch(key, field_name, value)

    def delete(self, key: int) -> None:
        """
        Deletes object from database table by integer key from Service layer.
        :param key: integer key (surrogate primary key)
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(key)

    def delete_all(self) -> None:
        """
        Deletes all objects from database table using Service layer.
        """
        self._service.delete_all()

general_controller = Blueprint('general_controller', __name__)

# @general_controller.route('/insert', methods=['POST'])
# def insert():
#     """
#     Обробник запиту для вставки даних через збережену процедуру.
#     """
#     data = request.json
#
#     # Перевірка, чи передані необхідні дані
#     if not data:
#         return jsonify({"error": "Немає даних у запиті"}), 400
#
#     table_name = data.get('table_name')
#     column_list = data.get('column_list')
#     value_list = data.get('value_list')
#
#     # Перевірка, чи всі параметри передані
#     if not table_name or not column_list or not value_list:
#         return jsonify({"error": "Відсутні необхідні параметри"}), 400
#
#     try:
#         # Виклик сервісу для вставки даних
#         insert_data(table_name, column_list, value_list)
#         return jsonify({"message": "Дані успішно вставлено"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
# animator_controller = Blueprint('animator_controller', __name__)
#
# @animator_controller.route('/add_animator_to_agency', methods=['POST'])
# def add_animator_to_agency_handler():
#     """
#     Обробник запиту для додавання аніматора до агенції через збережену процедуру.
#     """
#     data = request.json
#
#     if not data:
#         return jsonify({"error": "Немає даних у запиті"}), 400
#
#     animator_name = data.get('animator_name')
#     animator_last_name = data.get('animator_last_name')
#     agency_name = data.get('agency_name')
#
#     if not animator_name or not animator_last_name or not agency_name:
#         return jsonify({"error": "Відсутні необхідні параметри"}), 400
#
#     try:
#         add_animator_to_agency(animator_name, animator_last_name, agency_name)
#         return jsonify({"message": f"Animator '{animator_name} {animator_last_name}' успішно додано до агенції '{agency_name}'."}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
# noname_animator_controller = Blueprint('noname_animator_controller', __name__)
#
# @noname_animator_controller.route('/insert_noname_animators', methods=['POST'])
# def insert_noname_animators_route():
#     """
#     Обробник запиту для вставки 10 записів у таблицю animator через збережену процедуру.
#     """
#     try:
#         insert_noname_animators()
#         return jsonify({"message": "10 записів успішно вставлено у таблицю animator."}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
# mmas_controller = Blueprint('mmas_controller', __name__)
#
# @mmas_controller.route('/column-stat', methods=['POST'])
# def column_stat():
#     """
#     Обробник запиту для отримання статистики по колонці.
#     """
#     operation = request.json.get('operation')  # MAX, MIN, SUM, AVG
#
#     if not operation or len(operation) > 1000:
#         return jsonify({"error": "Невірна операція або її довжина перевищує 1000 символів"}), 400
#
#     if operation not in ['MAX', 'MIN', 'SUM', 'AVG']:
#         return jsonify({"error": "Невірна операція"}), 400
#
#     try:
#         stat_result = get_column_stat(operation)
#         if stat_result is None:
#             return jsonify({"error": "Не вдалося отримати статистику"}), 500
#         return jsonify({"stat_result": stat_result}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
# animator_distribute_controller = Blueprint('animator_distribute_controller', __name__)
#
# @animator_distribute_controller.route('/distribute_animators', methods=['POST'])
# def distribute_animators():
#     """
#     Обробник запиту для розподілу аніматорів у нові таблиці.
#     """
#     try:
#         distribute_animators_data()
#         return jsonify({"message": "Data successfully distributed into new tables!"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500