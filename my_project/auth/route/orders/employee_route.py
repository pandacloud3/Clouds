from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import employee_controller
from my_project.auth.domain.orders.Employee import Employee

employee_bp = Blueprint('employees', __name__, url_prefix='/employees')


@employee_bp.get('')
def get_all_employees() -> Response:
    """
    Gets all employees from the database.
    :return: Response object
    """
    employees = employee_controller.find_all()
    employees_dto = [emp.put_into_dto() for emp in employees]
    return make_response(jsonify(employees_dto), HTTPStatus.OK)


@employee_bp.post('')
def create_employee() -> Response:
    """
    Creates a new employee in the database.
    :return: Response object
    """
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.create(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED)


@employee_bp.get('/<int:employee_id>')
def get_employee(employee_id: int) -> Response:
    """
    Gets employee by ID.
    :param employee_id: ID of the employee
    :return: Response object
    """
    employee = employee_controller.find_by_id(employee_id)
    if employee:
        return make_response(jsonify(employee.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employee not found"}), HTTPStatus.NOT_FOUND)


@employee_bp.put('/<int:employee_id>')
def update_employee(employee_id: int) -> Response:
    """
    Updates employee by ID.
    :param employee_id: ID of the employee
    :return: Response object
    """
    content = request.get_json()
    employee = Employee.create_from_dto(content)
    employee_controller.update(employee_id, employee)
    return make_response("Employee updated", HTTPStatus.OK)


@employee_bp.delete('/<int:employee_id>')
def delete_employee(employee_id: int) -> Response:
    """
    Deletes employee by ID.
    :param employee_id: ID of the employee
    :return: Response object
    """
    employee_controller.delete(employee_id)
    return make_response("Employee deleted", HTTPStatus.NO_CONTENT)


@employee_bp.get('/lastname/<string:last_name>')
def get_employees_by_lastname(last_name: str) -> Response:
    """
    Gets employees by last name.
    :param last_name: Employee's last name
    :return: Response object
    """
    employees = employee_controller.find_by_lastname(last_name)
    return make_response(jsonify([emp.put_into_dto() for emp in employees]), HTTPStatus.OK)


@employee_bp.get('/gender/<string:gender>')
def get_employees_by_gender(gender: str) -> Response:
    """
    Gets employees by gender.
    :param gender: Employee's gender (e.g. Male/Female)
    :return: Response object
    """
    employees = employee_controller.find_by_gender(gender)
    return make_response(jsonify([emp.put_into_dto() for emp in employees]), HTTPStatus.OK)


@employee_bp.get('/position/<string:position>')
def get_employees_by_position(position: str) -> Response:
    """
    Gets employees by position.
    :param position: Employee's position
    :return: Response object
    """
    employees = employee_controller.find_by_position(position)
    return make_response(jsonify([emp.put_into_dto() for emp in employees]), HTTPStatus.OK)
