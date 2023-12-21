from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from database import Session
from qt.generated.ui_databasepage import Ui_DataBasePage
from model.models import Triangle
from utils.strateges.TriangleTableFillStrategy import TriangleTableFillStrategy


class DataBasePage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DataBasePage()
        self.ui.setupUi(self)
        self.session = Session()
        self.strategy = TriangleTableFillStrategy(self.ui.tableWidget)
        self.strategy.fill_table(self.session.query(Triangle).all())
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
        new_triangle = Triangle(first_side, second_side)
        self.session.add(new_triangle)
        self.session.commit()

        row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)

        self.strategy.insert_row(row, new_triangle)
        self.ui.tableWidget.repaint()

    def closeEvent(self, event: QCloseEvent):
        event.accept()
        self.parent().setEnabled(True)
