from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from utils.table_factory.ITable import ITable


class QtTable(ITable):
    def __init__(self, table: QTableWidget):
        self.table = table

    def render(self, data):
        self.table.setColumnCount(len(data[0]))
        pos_id = data[0].index('id')
        try:
            pos_id = data[0].index('id')
        except ValueError:
            pass
        self.table.setColumnHidden(pos_id, True)
        self.table.setHorizontalHeaderLabels(data[0])
        self.table.setRowCount(len(data) - 1)
        for row_index, row in enumerate(data[1:]):
            for column_index, item in enumerate(row):
                self.table.setItem(row_index, column_index, QTableWidgetItem(str(item)))
        return self.table

    def insert_row(self, data: list, row: int) -> QTableWidget | QTableWidget:
        self.table.setRowCount(self.table.rowCount() + 1)
        for i in range(0, self.table.columnCount()):
            self.table.setItem(row, i, QTableWidgetItem(str(data[i])))

