import sys
# os.system(r'''venv\Scripts\activate.bat
# pyside6-rcc views/res.qrc -o generated/res_rc.py
# .venv/Scripts/pyside6-uic views/MainWindow.ui > generated/ui_mainwindow.py
# .venv/Scripts/pyside6-uic views/DatabasePage.ui > generated/ui_databasepage.py'''.replace('/n', '&'))


from PySide6.QtWidgets import QApplication
from qt.windows.MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
