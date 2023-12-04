from PySide6.QtWidgets import QMainWindow

from generates.ui_databasepage import Ui_DataBasePage


class DataBasePage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DataBasePage()
        self.ui.setupUi(self)
        # code
        self.show()

    def closeEvent(self, event):
        event.accept()
        self.parent().setEnabled(True)