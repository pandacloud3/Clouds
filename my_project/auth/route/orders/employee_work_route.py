from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import employee_work_controller
from my_project.auth.domain.orders.EmployeeWork import EmployeeWork

employee_work_bp = Blueprint('employee_works', __name__, url_prefix='/employee_works')


@employee_work_bp.get('')
def get_all_employee_works() -> Response:
    """
    Gets all employee works from the database.
    :return: Response object
    """
    emp_works = employee_work_controller.find_all()
    emp_works_dto = [ew.put_into_dto() for ew in emp_works]
    return make_response(jsonify(emp_works_dto), HTTPStatus.OK)


@employee_work_bp.post('')
def create_employee_work() -> Response:
    """
    Creates a new employee_work record in the database.
    :return: Response object
    """
    content = request.get_json()
    emp_work = EmployeeWork.create_from_dto(content)
    employee_work_controller.create(emp_work)
    return make_response(jsonify(emp_work.put_into_dto()), HTTPStatus.CREATED)


@employee_work_bp.get('/<int:emp_work_id>')
def get_employee_work(emp_work_id: int) -> Response:
    """
    Gets employee_work by ID.
    :param emp_work_id: ID of the employee_work
    :return: Response object
    """
    emp_work = employee_work_controller.find_by_id(emp_work_id)
    if emp_work:
        return make_response(jsonify(emp_work.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employee_work not found"}), HTTPStatus.NOT_FOUND)


@employee_work_bp.put('/<int:emp_work_id>')
def update_employee_work(emp_work_id: int) -> Response:
    """
    Updates employee_work by ID.
    :param emp_work_id: ID of the employee_work
    :return: Response object
    """
    content = request.get_json()
    emp_work = EmployeeWork.create_from_dto(content)
    employee_work_controller.update(emp_work_id, emp_work)
    return make_response("Employee_work updated", HTTPStatus.OK)


@employee_work_bp.delete('/<int:emp_work_id>')
def delete_employee_work(emp_work_id: int) -> Response:
    """
    Deletes employee_work by ID.
    :param emp_work_id: ID of the employee_work
    :return: Response object
    """
    employee_work_controller.delete(emp_work_id)
    return make_response("Employee_work deleted", HTTPStatus.NO_CONTENT)


@employee_work_bp.get('/employee/<int:employee_id>')
def get_works_by_employee(employee_id: int) -> Response:
    """
    Gets all works assigned to a specific employee.
    :param employee_id: ID of the employee
    :return: Response object
    """
    works = employee_work_controller.find_by_employee_id(employee_id)
    return make_response(jsonify([w.put_into_dto() for w in works]), HTTPStatus.OK)


@employee_work_bp.get('/work/<int:work_id>')
def get_employees_by_work(work_id: int) -> Response:
    """
    Gets all employees assigned to a specific work type.
    :param work_id: ID of the type of work
    :return: Response object
    """
    employees = employee_work_controller.find_by_work_id(work_id)
    return make_response(jsonify([e.put_into_dto() for e in employees]), HTTPStatus.OK)
