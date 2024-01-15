from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from qt.generated.ui_databasepage import Ui_DataBasePage
from model.models import Triangle
from model.builder import TriangleBuilder
from utils.strateges.TriangleTableStrategy import TriangleTableStrategy

from utils.table_factory.QtTable import QtTable
from utils.table_factory.TableFactory import TableFactory


class DataBasePage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DataBasePage()
        self.ui.setupUi(self)
        self.columns_names = ["id", "Первая сторона", "Вторая сторона"]
        self.table = TableFactory().create_table('qt', self.ui.tableWidget)
        self.strategy = TriangleTableStrategy(self.table)
        self.strategy.fill_table(self.columns_names)
        self.ui.tableWidget.cellChanged.connect(self.dataChange)
        self.ui.tableWidget.itemDoubleClicked.connect(self.importData)
        self.ui.addRecBtn.clicked.connect(self.createTriangle)
        # code
        self.show()

    def dataChange(self, row: int, col: int):
        item = self.ui.tableWidget.item(row, col)
        if item is not None:
            data = [float(self.ui.tableWidget.item(row, 0).text()), col, float(item.text())]
            self.strategy.update_row(data, row)

    def importData(self, item: QTableWidgetItem):
        row = item.row()
        self.parent().ui.firstSideNum.setValue(float(self.ui.tableWidget.item(row, 1).text()))
        self.parent().ui.secondSideNum.setValue(float(self.ui.tableWidget.item(row, 2).text()))
        self.parent().setEnabled(True)
        self.close()

    def createTriangle(self):
        first_side = self.ui.cntCatet1.value()
        second_side = self.ui.cntCatet2.value()
        row = self.ui.tableWidget.rowCount()
        self.strategy.insert_row([first_side, second_side], row)
        self.ui.tableWidget.selectRow(row)

    def closeEvent(self, event: QCloseEvent):
        event.accept()
        self.parent().setEnabled(True)
