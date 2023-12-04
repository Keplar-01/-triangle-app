from PySide6.QtCore import QFile, QTextStream
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from generates.ui_mainwindow import Ui_MainWindow
from utils.Triangle import RightTriangle
from windows.DataBasePage import DataBasePage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.calculateBtn.clicked.connect(self.calculate)
        self.ui.fileBtn.clicked.connect(self.readFromFile)
        self.ui.databaseBtn.clicked.connect(self.openDatabasePage)
        # code
        self.show()

    def calculate(self):
        trio = RightTriangle(self.ui.firstSideNum.value(), self.ui.secondSideNum.value())
        self.ui.Hyp.setText(f'{trio.hypotenuse}')
        self.ui.perimetr.setText(f'{trio.perimeter}')
        self.ui.area.setText(f'{trio.area}')

    def readFromFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Текстовые файлы (*.txt);;Все файлы (*)",
                                                   options=options)
        with open(file_name, 'r') as file:
            content = file.readline().strip()
            try:
                firstSide, secondSide = map(float, content.split())
                self.ui.firstSideNum.setValue(firstSide)
                self.ui.secondSideNum.setValue(secondSide)
            except ValueError as e:
                QMessageBox.critical(self, "Ошибка", f"Ошибка при чтении файла, убедитесь, что в строке лежат два "
                                                     f"числа разделенных пробелом")


    def openDatabasePage(self):
        self.setDisabled(True)
        a = DataBasePage(self)
        a.show()

