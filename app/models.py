from sqlalchemy import Column, Integer, String

from .db import Base

class URL(Base):
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True)
    short = Column(String, unique=True, index=True)
    target = Column(String, index=True)