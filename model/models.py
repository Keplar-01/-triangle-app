from sqlalchemy import Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Triangle(Base):
    __tablename__ = 'triangles'

    id = Column(Integer, primary_key=True)
    first_side = Column(Float)
    second_side = Column(Float)

    @property
    def hypotenuse(self) -> float:
        return (self.first_side ** 2 + self.second_side ** 2) ** 0.5

    @property
    def area(self) -> float:
        return self.first_side * self.second_side / 2

    @property
    def perimeter(self) -> float:
        return self.first_side + self.second_side + self.hypotenuse

    def __str__(self) -> str:
        return f'A={self.first_side} B={self.second_side} C={self.hypotenuse}'
