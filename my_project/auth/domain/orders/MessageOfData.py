from __future__ import annotations
from typing import Dict, Any
from datetime import time, date

from my_project import db
from my_project.auth.domain.i_dto import IDto


class MessageOfData(db.Model, IDto):
    """
    Association table between Meteostation and Data.
    Many-to-Many relationship with additional attributes: date and time.
    """
    __tablename__ = "message_of_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.Time, nullable=False)
    date = db.Column(db.Date, nullable=False)
    data_id = db.Column(db.Integer, db.ForeignKey("data.id"), nullable=False)
    meteostation_id = db.Column(db.Integer, db.ForeignKey("meteostation.id"), nullable=False)

    # Зворотні зв'язки
    data = db.relationship("Data", backref="message_links", lazy=True)
    meteostation = db.relationship("Meteostation", backref="message_links", lazy=True)

    def __repr__(self) -> str:
        return (
            f"MessageOfData(id={self.id}, time='{self.time}', date='{self.date}', "
            f"data_id={self.data_id}, meteostation_id={self.meteostation_id})"
        )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "time": str(self.time),
            "date": str(self.date),
            "data_id": self.data_id,
            "meteostation_id": self.meteostation_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MessageOfData:
        obj = MessageOfData(**dto_dict)
        return obj
