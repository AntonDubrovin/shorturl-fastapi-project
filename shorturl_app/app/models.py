from sqlalchemy import Column, Integer, String
from app.database import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    full_url = Column(String, index=True)
    short_url = Column(String, index=True, unique=True)
