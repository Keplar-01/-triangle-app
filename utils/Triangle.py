class RightTriangle:
    def __init__(self, first_side: float, second_side: float) -> None:
        self.__first_side = first_side
        self.__second_side = second_side

    def get_first_side(self) -> float:
        return self.__first_side

    def get_second_side(self) -> float:
        return self.__second_side

    @property
    def hypotenuse(self) -> float:
        return (self.__first_side ** 2 + self.__second_side ** 2) ** 0.5

    @property
    def area(self) -> float:
        return self.__first_side * self.__second_side / 2

    @property
    def perimeter(self) -> float:
        return self.__first_side + self.__second_side + self.hypotenuse

    def __str__(self) -> str:
        return f'A={self.__first_side} B={self.__second_side} C={self.hypotenuse}'