from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class TypeWork(db.Model, IDto):
    """
    Model declaration for TypeWork.
    """
    __tablename__ = "type_work"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(255), nullable=False)  # назва типу роботи

    # зв’язок один-до-багатьох: один тип роботи -> багато сервісних робіт
    service_works = db.relationship("ServiceWork", backref="type_work", lazy=True)

    def __repr__(self) -> str:
        return f"TypeWork({self.id}, '{self.type}')"

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
    def create_from_dto(dto_dict: Dict[str, Any]) -> TypeWork:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = TypeWork(**dto_dict)
        return obj
