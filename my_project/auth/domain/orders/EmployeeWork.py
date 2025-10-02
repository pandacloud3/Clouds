from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class EmployeeWork(db.Model, IDto):
    """
    Association table between Employee and ServiceWork.
    Many-to-Many relationship.
    """
    __tablename__ = "employee_work"

    employee_id = db.Column(db.Integer, db.ForeignKey("employee.id"), primary_key=True)
    work_id = db.Column(db.Integer, db.ForeignKey("service_work.id"), primary_key=True)

    # Зворотні зв'язки для ORM
    # employee = db.relationship("Employee", backref="employee_links")
    # service_work = db.relationship("ServiceWork", back_populates="employees")

    def __repr__(self) -> str:
        return f"EmployeeWork(employee_id={self.employee_id}, work_id={self.work_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts association object into DTO.
        :return: DTO object as dictionary
        """
        return {
            "employee_id": self.employee_id,
            "work_id": self.work_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EmployeeWork:
        """
        Creates association object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = EmployeeWork(**dto_dict)
        return obj
