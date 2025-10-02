from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Employee(db.Model, IDto):
    """
    Model declaration for Employee.
    """
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)   # ім’я
    last_name = db.Column(db.String(255), nullable=False)    # прізвище
    gender_id = db.Column(db.Integer, db.ForeignKey("gender.id"), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    phone_number = db.Column(db.String(50), nullable=True)

    # Many-to-Many через employee_work
    # service_works = db.relationship(
    #     "ServiceWork",
    #     secondary="employee_work",
    #     back_populates="employees",
    # )

    def __repr__(self) -> str:
        return (
            f"Employee({self.id}, '{self.first_name}', '{self.last_name}', "
            f"{self.gender_id}, '{self.email}', '{self.phone_number}')"
        )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender_id": self.gender_id,
            "email": self.email,
            "phone_number": self.phone_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employee:
        obj = Employee(**dto_dict)
        return obj
