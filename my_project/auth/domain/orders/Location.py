from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Location(db.Model, IDto):
    """
    Model declaration for Location.
    """
    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(255), nullable=False)  # назва локації
    stat = db.Column(db.String(255), nullable=True)       # стан або статус

    # Many-to-Many зв'язок з Meteostation
    meteostations = db.relationship(
        "Meteostation",
        secondary="meteostation_location",
        back_populates="locations"
    )

    def __repr__(self) -> str:
        return f"Location({self.id}, '{self.location}', '{self.stat}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "location": self.location,
            "stat": self.stat,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Location:
        obj = Location(**dto_dict)
        return obj
