from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class MeteostationLocation(db.Model, IDto):
    """
    Association table between Meteostation and Location.
    Many-to-Many relationship.
    """
    __tablename__ = "meteostation_location"

    meteostation_id = db.Column(db.Integer, db.ForeignKey("meteostation.id"), primary_key=True)
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"), primary_key=True)

    # Зворотні зв'язки для ORM
    meteostation = db.relationship("Meteostation", backref="location_links", lazy=True)
    location = db.relationship("Location", backref="meteostation_links", lazy=True)

    def __repr__(self) -> str:
        return f"MeteostationLocation(meteostation_id={self.meteostation_id}, location_id={self.location_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts association object into DTO.
        :return: DTO object as dictionary
        """
        return {
            "meteostation_id": self.meteostation_id,
            "location_id": self.location_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MeteostationLocation:
        """
        Creates association object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = MeteostationLocation(**dto_dict)
        return obj
