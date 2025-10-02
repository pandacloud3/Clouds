"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from abc import ABC
from typing import List

from sqlalchemy import inspect
from sqlalchemy.orm import Mapper

from my_project import db
# import mysql.connector
# from mysql.connector import Error


class GeneralDAO(ABC):
    """
    The common realization of Data Access class.
    """
    _domain_type = None
    _session = db.session

    def find_all(self) -> List[object]:
        """
        Gets all objects from table.
        :return: list of all objects
        """
        return self._session.query(self._domain_type).all()

    def find_by_id(self, key: int) -> object:
        """
        Gets object from database table by integer key.
        :param key: integer key (surrogate primary key)
        :return: search object
        """
        return self._session.query(self._domain_type).get(key)

    def create(self, obj: object) -> object:
        """
        Creates object in database table.
        :param obj: object to create in Database
        :return: created object
        """
        self._session.add(obj)
        self._session.commit()
        return obj

    def create_all(self, obj_list: List[object]) -> List[object]:
        """
        Creates objects from object list.
        :param obj_list: object list to create in Database
        :return: list of created object
        """
        self._session.add_all(obj_list)
        self._session.commit()
        return obj_list

    def update(self, key: int, in_obj: object) -> None:
        """
        Updates object in database table
        :param key: integer key (surrogate primary key)
        :param in_obj: object to update in Database
        """
        domain_obj = self._session.query(self._domain_type).get(key)
        mapper: Mapper = inspect(type(in_obj))  # Metadata
        columns = mapper.columns._collection
        for column_name, column_obj, *_ in columns:
            if not column_obj.primary_key:
                value = getattr(in_obj, column_name)
                setattr(domain_obj, column_name, value)
        self._session.commit()

    def patch(self, key: int, field_name: str, value: object) -> None:
        """
        Modifies defined field of object in database table.
        :param key: integer key (surrogate primary key)
        :param field_name: field name of object
        :param value: field value of object
        """
        domain_obj = self._session.query(self._domain_type).get(key)
        setattr(domain_obj, field_name, value)
        self._session.commit()

    def delete(self, key: int) -> None:
        """
        Deletes object from database table by integer key.
        :param key: integer key (surrogate primary key)
        """
        domain_obj = self._session.query(self._domain_type).get(key)
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise 

    def delete_all(self) -> None:
        """
        Deletes all objects from database table.
        """
        self._session.query(self._domain_type).delete()
        self._session.commit()

#Процедурка для вставки даних у таблиці
# def call_insert_procedure(table_name, column_list, value_list):
#     """
#     Викликає збережену процедуру `insert_into_table` у базі даних MySQL.
#     """
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='a4b8c11g3',
#             database='lab3'
#         )
#         cursor = connection.cursor()
#
#         procedure_call = "CALL insert_into_table(%s, %s, %s)"
#
#         cursor.execute(procedure_call, (table_name, column_list, value_list))
#         connection.commit()
#         print(f"Дані успішно вставлені в таблицю {table_name}.")
#
#     except mysql.connector.Error as error:
#         print(f"Помилка під час виклику процедурки: {error}")
#         raise error
#
#     finally:
#
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
#
# def call_add_animator_to_agency(animator_name, animator_last_name, agency_name):
#     """
#     Викликає збережену процедуру AddAnimatorToAgency у базі даних MySQL.
#     """
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='a4b8c11g3',
#             database='lab3'
#         )
#         cursor = connection.cursor()
#
#         procedure_call = "CALL AddAnimatorToAgency(%s, %s, %s)"
#
#         cursor.execute(procedure_call, (animator_name, animator_last_name, agency_name))
#         connection.commit()
#         print(f"Animator '{animator_name} {animator_last_name}' успішно додано до агенції '{agency_name}'.")
#
#     except mysql.connector.Error as error:
#         print(f"Помилка під час виклику процедурки: {error}")
#         raise error
#
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
# def call_insert_noname_animators():
#     """
#     Викликає збережену процедуру InsertNonameAnimators у базі даних MySQL.
#     """
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='a4b8c11g3',
#             database='lab3'
#         )
#         cursor = connection.cursor()
#
#         cursor.execute("CALL InsertNonameAnimators()")
#         connection.commit()
#         print("10 записів успішно вставлено у таблицю animator.")
#
#     except mysql.connector.Error as error:
#         print(f"Помилка під час виклику процедурки: {error}")
#         raise error
#
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
# import mysql.connector
#
# def call_get_column_stat(operation):
#     """
#     Викликає збережену процедуру CallColumnStat в базі даних MySQL
#     для отримання статистики по колонці.
#     """
#     connection = None
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='a4b8c11g3',
#             database='lab3'
#         )
#         cursor = connection.cursor()
#
#         cursor.callproc('CallColumnStat', [operation])
#
#         for result in cursor.stored_results():
#             stat_result = result.fetchone()
#             return stat_result[0] if stat_result else None
#
#     except mysql.connector.Error as error:
#         print(f"Помилка під час виклику процедури: {error}")
#         raise error
#
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
# import mysql.connector
# from mysql.connector import Error
#
# def create_connection():
#     """
#     Створює з'єднання з базою даних MySQL.
#     """
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='a4b8c11g3',
#             database='lab3'
#         )
#         if connection.is_connected():
#             return connection
#     except Error as e:
#         print(f"Помилка під час підключення до MySQL: {e}")
#         raise
#
# def create_random_animator_tables():
#     """
#     Викликає збережену процедуру для створення таблиць і копіювання даних.
#     """
#     connection = None
#     try:
#         connection = create_connection()
#         cursor = connection.cursor()
#
#         cursor.callproc('CreateRandomAnimatorTablesAndCopyData')
#
#         connection.commit()
#
#     except mysql.connector.Error as error:
#         print(f"Помилка під час виклику процедури: {error}")
#         raise error
#     finally:
#         if connection and connection.is_connected():
#             cursor.close()
#             connection.close()
