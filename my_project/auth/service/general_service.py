"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from abc import ABC
from typing import List
# from my_project.auth.dao.general_dao import call_insert_procedure
# from my_project.auth.dao.general_dao import call_add_animator_to_agency
# from my_project.auth.dao.general_dao import call_insert_noname_animators
# from my_project.auth.dao.general_dao import call_get_column_stat
# from my_project.auth.dao.general_dao import create_random_animator_tables

class GeneralService(ABC):
    """
    The common realization of the Business Layer.
    """
    _dao = None

    def find_all(self) -> List[object]:
        """
        Gets all objects from table using Data Access layer.
        :return: list of all objects
        """
        return self._dao.find_all()

    def find_by_id(self, key: int) -> object:
        """
        Gets object from database table by integer key using from Data Access layer.
        :param key: integer key (surrogate primary key)
        :return: search object
        """
        return self._dao.find_by_id(key)

    def create(self, obj: object) -> object:
        """
        Creates object in database table using Data Access layer.
        :param obj: object to create in Database
        :return: created object
        """
        return self._dao.create(obj)

    def create_all(self, obj_list: List[object]) -> List[object]:
        """
        Creates objects from object list using Data Access layer.
        :param obj_list: object list to create in Database
        :return: list of created object
        """
        return self._dao.create_all(obj_list)

    def update(self, key: int, obj: object) -> None:
        """
        Updates object in database table using Data Access layer.
        :param key: integer key (surrogate primary key)
        :param obj: object to create in Database
        """
        self._dao.update(key, obj)

    def patch(self, key: int, field_name: str, value: object) -> None:
        """
        Modifies defined field of object in database table using Data Access layer.
        :param key: integer key (surrogate primary key)
        :param field_name: field name of object
        :param value: field value of object
        """
        self._dao.patch(key, field_name, value)

    def delete(self, key: int) -> None:
        """
        Deletes object from database table by integer key from Data Access layer.
        :param key: integer key (surrogate primary key)
        """
        self._dao.delete(key)

    def delete_all(self) -> None:
        """
        Deletes all objects from database table using Data Access layer.
        """
        self._dao.delete_all()

# def insert_data(table_name, column_list, value_list):
#     """
#     Сервісний рівень для виклику процедури.
#     """
#     try:
#         call_insert_procedure(table_name, column_list, value_list)
#     except Exception as e:
#         print(f"Помилка на рівні сервісу: {e}")
#         raise
#
# def add_animator_to_agency(animator_name, animator_last_name, agency_name):
#     """
#     Сервісний рівень для виклику процедури AddAnimatorToAgency.
#     """
#     try:
#         call_add_animator_to_agency(animator_name, animator_last_name, agency_name)
#     except Exception as e:
#         print(f"Помилка на рівні сервісу: {e}")
#         raise
# def insert_noname_animators():
#     """
#     Сервісний рівень для виклику процедури InsertNonameAnimators.
#     """
#     try:
#         call_insert_noname_animators()
#     except Exception as e:
#         print(f"Помилка на рівні сервісу: {e}")
#         raise
# def get_column_stat(operation):
#     """
#     Сервіс для отримання статистики по колонці з бази даних.
#     """
#     try:
#         return call_get_column_stat(operation)
#     except Exception as e:
#         print(f"Помилка на рівні сервісу: {e}")
#         raise
#
# def distribute_animators_data():
#     """
#     Викликає DAO для розподілу даних у нові таблиці.
#     """
#     try:
#         create_random_animator_tables()
#     except Exception as e:
#         print(f"Помилка на рівні сервісу: {e}")
#         raise
