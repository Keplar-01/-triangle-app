import os
import subprocess
import sys

from PySide6.QtWidgets import QApplication
from windows.MainWindow import MainWindow



# os.system(r'''venv\Scripts\activate.bat
# pyside6-rcc resources/res.qrc -o generated/res_rc.py
# .venv/Scripts/pyside6-uic resources/MainWindow.ui > generated/ui_mainwindow.py
# .venv/Scripts/pyside6-uic resources/DatabasePage.ui > generated/ui_databasepage.py'''.replace('/n', '&'))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
