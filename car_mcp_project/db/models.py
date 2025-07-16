from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    engine = Column(String, nullable=False)
    fuel = Column(String, nullable=False)
    color = Column(String, nullable=False)
    mileage = Column(Integer, nullable=False)
    doors = Column(Integer, nullable=False)
    transmission = Column(String, nullable=False)
    price = Column(Float, nullable=False)

def get_engine():
    return create_engine('sqlite:///cars.db')
