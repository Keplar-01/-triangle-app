from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Triangle(Base):
    __tablename__ = 'triangles'

    id = Column(Integer, primary_key=True)
    first_side = Column(Float)
    second_side = Column(Float)

    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side
