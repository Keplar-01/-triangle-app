import os
import sys

os.system('''pyside6-rcc res.qrc -o res_rc.py
pyside6-uic MainWindow.ui > ui_mainwindow.py'''.replace('\n', '&'))

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # code
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
