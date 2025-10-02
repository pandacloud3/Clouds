from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Gender(db.Model, IDto):
    """
    Model declaration for Gender.
    """
    __tablename__ = "gender"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(255), nullable=False)  # назва гендеру

    # зв'язок один-до-багатьох: один гендер -> багато працівників
    employees = db.relationship("Employee", backref="gender", lazy=True)

    def __repr__(self) -> str:
        return f"Gender({self.id}, '{self.type}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO.
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "type": self.type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Gender:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Gender(**dto_dict)
        return obj
