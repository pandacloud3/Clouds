from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Producer(db.Model, IDto):
    """
    Model declaration for Producer.
    """
    __tablename__ = "producer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)     # назва виробника
    address = db.Column(db.String(255), nullable=True)   # адреса виробника

    # зв’язок один-до-багатьох: один виробник -> багато метеостанцій
    meteostations = db.relationship("Meteostation", backref="producer", lazy=True)

    def __repr__(self) -> str:
        return f"Producer({self.id}, '{self.name}', '{self.address}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Producer:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Producer(**dto_dict)
        return obj
