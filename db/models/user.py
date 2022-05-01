
from sqlalchemy import Column, Integer, String, Sequence
from db.models import DB


class UserModel(DB.Base):
    __tablename__ = __name__
    # ID (Primary key)
    id = Column(String, primary_key=True)
    name = Column(String(20))

    def __init__(self, id: str, name: str = "") -> None:
        self.id = id
        self.name = name
