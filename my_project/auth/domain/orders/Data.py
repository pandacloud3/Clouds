from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Data(db.Model, IDto):
    """
    Model declaration for Data collected from Meteostation.
    """
    __tablename__ = "data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    meteostation_id = db.Column(db.Integer, db.ForeignKey("meteostation.id"), nullable=False)
    temperature = db.Column(db.Float, nullable=True)
    wind_speed = db.Column(db.Float, nullable=True)
    humidity = db.Column(db.Float, nullable=True)
    wind_direction = db.Column(db.Float, nullable=True)
    atm_pressure = db.Column(db.Float, nullable=True)
    date = db.Column(db.Date, nullable=False)

    # Зворотний зв'язок до Meteostation
    meteostation = db.relationship("Meteostation", backref="data_records", lazy=True)

    meteostations_m2m = db.relationship(
        "Meteostation",
        secondary="message_of_data",
        back_populates="data_records_m2m"
    )

    def __repr__(self) -> str:
        return (
            f"Data({self.id}, meteostation_id={self.meteostation_id}, "
            f"temperature={self.temperature}, wind_speed={self.wind_speed}, "
            f"humidity={self.humidity}, wind_direction={self.wind_direction}, "
            f"atm_pressure={self.atm_pressure}, date='{self.date}')"
        )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "meteostation_id": self.meteostation_id,
            "temperature": self.temperature,
            "wind_speed": self.wind_speed,
            "humidity": self.humidity,
            "wind_direction": self.wind_direction,
            "atm_pressure": self.atm_pressure,
            "date": str(self.date),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Data:
        obj = Data(**dto_dict)
        return obj
