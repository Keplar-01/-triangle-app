from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from database import Session
from qt.generated.ui_databasepage import Ui_DataBasePage
from model.models import Triangle
from model.builder import TriangleBuilder
from utils.strateges.TriangleTableFillStrategy import TriangleTableFillStrategy
from utils.table_factory.QtTable import QtTable
from utils.table_factory.TableFactory import TableFactory


class DataBasePage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DataBasePage()
        self.ui.setupUi(self)
        self.session = Session()
        self.columns_names = ["id", "Первая сторона", "Вторая сторона"]
        self.table = TableFactory().create_table('qt', self.ui.tableWidget)
        self.strategy = TriangleTableFillStrategy(self.table)
        self.strategy.fill_table(self.columns_names)
        self.ui.tableWidget.cellChanged.connect(self.dataChange)
        self.ui.tableWidget.itemDoubleClicked.connect(self.importData)
        self.ui.addRecBtn.clicked.connect(self.createTriangle)
        # code
        self.show()

    def dataChange(self, row: int, col: int):
        item = self.ui.tableWidget.item(row, col)
        if item is not None:
            triangle_id = int(self.ui.tableWidget.item(row, 0).text())
            if col == 1:
                self.session.query(Triangle).filter_by(id=triangle_id).update({Triangle.first_side: float(item.text())})
            elif col == 2:
                self.session.query(Triangle).filter_by(id=triangle_id).update({Triangle.second_side: float(item.text())})
            self.session.commit()

    def importData(self, item: QTableWidgetItem):
        row = item.row()
        print(row)
        self.parent().ui.firstSideNum.setValue(float(self.ui.tableWidget.item(row, 1).text()))
        self.parent().ui.secondSideNum.setValue(float(self.ui.tableWidget.item(row, 2).text()))
        self.parent().setEnabled(True)
        self.close()

    def createTriangle(self):
        first_side = self.ui.cntCatet1.value()
        second_side = self.ui.cntCatet2.value()
        builder = TriangleBuilder()
        triangle = builder.set_first_side(first_side).set_second_side(second_side).get_triangle()
        self.session.add(triangle)
        self.session.commit()

        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
        self.insert_row(row, triangle)
        self.ui.tableWidget.repaint()

    def insert_row(self, row: int, triangle: Triangle) -> None:
        item_id = QTableWidgetItem(str(triangle.id))
        item_first_side = QTableWidgetItem(str(triangle.first_side))
        item_second_side = QTableWidgetItem(str(triangle.second_side))

        self.ui.tableWidget.setItem(row, 0, item_id)
        self.ui.tableWidget.setItem(row, 1, item_first_side)
        self.ui.tableWidget.setItem(row, 2, item_second_side)
    def closeEvent(self, event: QCloseEvent):
        event.accept()
        self.parent().setEnabled(True)
