from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from database import Session
from model.models import Triangle
from utils.strateges.IFigureTableFillStrategy import IFigureTableFillStrategy
from utils.table_factory.ITable import ITable


class TriangleTableFillStrategy(IFigureTableFillStrategy):
    column_names = ["id", "Первая сторона", "Вторая сторона"]

    def __init__(self, table: ITable):
        super().__init__()
        self.table = table
        self.session = Session()

    def prepare_data(self):
        data = self.session.query(Triangle).all()
        table_data = []
        table_data.append(self.column_names)
        for triangle in data:
            row = [triangle.id, triangle.first_side, triangle.second_side, triangle.hypotenuse, triangle.perimeter, triangle.area]
            table_data.append(row)
        return table_data

    def fill_table(self) -> None:
        self.table.render(self.prepare_data())
