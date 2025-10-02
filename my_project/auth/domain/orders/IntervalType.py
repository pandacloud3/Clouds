from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class IntervalType(db.Model, IDto):
    """
    Model declaration for IntervalType.
    """
    __tablename__ = "interval_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(255), nullable=False)  # назва типу інтервалу

    # зв’язок один-до-багатьох: один тип інтервалу -> багато метеостанцій
    meteostations = db.relationship("Meteostation", backref="interval_type", lazy=True)

    def __repr__(self) -> str:
        return f"IntervalType({self.id}, '{self.type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "type": self.type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> IntervalType:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = IntervalType(**dto_dict)
        return obj
