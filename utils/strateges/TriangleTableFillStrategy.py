from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from database import Session
from model.models import Triangle
from utils.strateges.IFigureTableFillStrategy import IFigureTableFillStrategy


class TriangleTableFillStrategy(IFigureTableFillStrategy):
    column_names = ["id", "Первая сторона", "Вторая сторона"]

    def __init__(self, table: QTableWidget):
        super().__init__()
        self.table = table

    def set_up_columns(self, column_names: list[str]) -> None:
        self.table.setColumnCount(len(column_names))
        self.table.setHorizontalHeaderLabels(column_names)
        if column_names.index('id') != -1:
            self.table.setColumnHidden(column_names.index('id'), True)

    def insert_row(self, row: int, triangle: Triangle) -> None:
        item_id = QTableWidgetItem(str(triangle.id))
        item_first_side = QTableWidgetItem(str(triangle.first_side))
        item_second_side = QTableWidgetItem(str(triangle.second_side))

        self.table.setItem(row, 0, item_id)
        self.table.setItem(row, 1, item_first_side)
        self.table.setItem(row, 2, item_second_side)

    def set_up_rows(self, data: list[Triangle]) -> None:
        self.table.setRowCount(len(data))
        for row, triangle in enumerate(data):
            self.insert_row(row, triangle)

    def fill_table(self) -> None:
        data = Session().query(Triangle).all()
        self.set_up_columns(self.column_names)
        self.set_up_rows(data)
