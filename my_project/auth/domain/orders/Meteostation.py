from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Meteostation(db.Model, IDto):
    """
    Model declaration for Meteostation.
    """
    __tablename__ = "meteostation"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"), nullable=True)
    producer_id = db.Column(db.Integer, db.ForeignKey("producer.id"), nullable=True)
    installation_date = db.Column(db.Date, nullable=True)
    interval_id = db.Column(db.Integer, db.ForeignKey("interval_type.id"), nullable=True)

    data_records_m2m = db.relationship(
        "Data",
        secondary="message_of_data",
        back_populates="meteostations_m2m"
    )

    locations = db.relationship(
        "Location",
        secondary="meteostation_location",
        back_populates="meteostations"
    )

    def __repr__(self) -> str:
        return (
            f"Meteostation({self.id}, '{self.name}', '{self.location_id}', "
            f"{self.producer_id}, '{self.installation_date}', {self.interval_id})"
        )

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "location_id": self.location_id,
            "producer_id": self.producer_id,
            "installation_date": str(self.installation_date),
            "interval_id": self.interval_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Meteostation:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Meteostation(**dto_dict)
        return obj
