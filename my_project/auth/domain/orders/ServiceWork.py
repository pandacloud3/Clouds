from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class ServiceWork(db.Model, IDto):
    """
    Model declaration for ServiceWork.
    """
    __tablename__ = "service_work"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date, nullable=False)
    meteostation_id = db.Column(db.Integer, db.ForeignKey("meteostation.id"), nullable=False)
    type_work_id = db.Column(db.Integer, db.ForeignKey("type_work.id"), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    # зв’язки
    # meteostation = db.relationship("Meteostation", backref="service_works", lazy=True)
    # type_work = db.relationship("TypeWork", backref="service_works", lazy=True)
    # employees = db.relationship(
    #     "Employee",
    #     secondary="employee_work",
    #     back_populates="service_works",
    # )

    def __repr__(self) -> str:
        return (
            f"ServiceWork({self.id}, '{self.date}', {self.meteostation_id}, "
            f"{self.type_work_id}, '{self.description}')"
        )

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "date": str(self.date),
            "meteostation_id": self.meteostation_id,
            "type_work_id": self.type_work_id,
            "description": self.description,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ServiceWork:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = ServiceWork(**dto_dict)
        return obj
