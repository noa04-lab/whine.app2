from sqlalchemy import Column, Integer, String, Float
from database import Base

class Wine(Base):
    __tablename__ = "wines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    region = Column(String)
    year = Column(Integer)
    price = Column(Float)
