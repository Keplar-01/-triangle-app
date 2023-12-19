from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

from database import engine, Session
from generated.ui_databasepage import Ui_DataBasePage
from model.models import Triangle


class DataBasePageController(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DataBasePage()
        self.ui.setupUi(self)
        self.getDataTable()
        self.ui.tableWidget.cellChanged.connect(self.dataChange)
        self.ui.tableWidget.itemDoubleClicked.connect(self.importData)
        self.ui.addRecBtn.clicked.connect(self.createTriangle)
        # code
        self.show()

    def getDataTable(self):
        session = Session()
        triangles = session.query(Triangle).all()
        self.ui.tableWidget.setRowCount(len(triangles))
        self.ui.tableWidget.setColumnHidden(0, True)
        for row, triangle in enumerate(triangles):
            self.insertRow(triangle, row)

    def dataChange(self, row: int, col: int):
        session = Session()
        item = self.ui.tableWidget.item(row, col)
        if item is not None:
            triangle_id = int(self.ui.tableWidget.item(row, 0).text())
            if col == 1:
                session.query(Triangle).filter_by(id=triangle_id).update({Triangle.first_side: float(item.text())})
            elif col == 2:
                session.query(Triangle).filter_by(id=triangle_id).update({Triangle.second_side: float(item.text())})
            session.commit()

    def createTriangle(self):
        session = Session()
        first_side = self.ui.cntCatet1.value()
        second_side = self.ui.cntCatet2.value()
        new_triangle = Triangle(first_side, second_side)
        session.add(new_triangle)
        session.commit()

        new_row_index = self.ui.tableWidget.rowCount()

        self.ui.tableWidget.insertRow(new_row_index)
        self.insertRow(new_triangle, new_row_index)

    def importData(self, item: QTableWidgetItem):
        row = item.row()
        print(row)
        self.parent().ui.firstSideNum.setValue(float(self.ui.tableWidget.item(row, 1).text()))
        self.parent().ui.secondSideNum.setValue(float(self.ui.tableWidget.item(row, 2).text()))
        self.parent().setEnabled(True)
        self.close()

    def insertRow(self, triangle: Triangle, row: int):
        item_id = QTableWidgetItem(str(triangle.id))
        item_first_side = QTableWidgetItem(str(triangle.first_side))
        item_second_side = QTableWidgetItem(str(triangle.second_side))

        self.ui.tableWidget.setItem(row, 0, item_id)
        self.ui.tableWidget.setItem(row, 1, item_first_side)
        self.ui.tableWidget.setItem(row, 2, item_second_side)

    def closeEvent(self, event: QCloseEvent):
        event.accept()
        self.parent().setEnabled(True)
