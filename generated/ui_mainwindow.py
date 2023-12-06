# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(350, 200)
        icon = QIcon()
        iconThemeName = u":/newPrefix/icon.ico"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.fileBtn = QPushButton(self.centralwidget)
        self.fileBtn.setObjectName(u"fileBtn")

        self.gridLayout.addWidget(self.fileBtn, 5, 2, 1, 1)

        self.firstSideNum = QDoubleSpinBox(self.centralwidget)
        self.firstSideNum.setObjectName(u"firstSideNum")

        self.gridLayout.addWidget(self.firstSideNum, 0, 1, 1, 2)

        self.Hyp = QLabel(self.centralwidget)
        self.Hyp.setObjectName(u"Hyp")

        self.gridLayout.addWidget(self.Hyp, 2, 1, 1, 2)

        self.secondSideNum = QDoubleSpinBox(self.centralwidget)
        self.secondSideNum.setObjectName(u"secondSideNum")

        self.gridLayout.addWidget(self.secondSideNum, 1, 1, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.databaseBtn = QPushButton(self.centralwidget)
        self.databaseBtn.setObjectName(u"databaseBtn")

        self.gridLayout.addWidget(self.databaseBtn, 5, 1, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.calculateBtn = QPushButton(self.centralwidget)
        self.calculateBtn.setObjectName(u"calculateBtn")

        self.gridLayout.addWidget(self.calculateBtn, 5, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.area = QLabel(self.centralwidget)
        self.area.setObjectName(u"area")

        self.gridLayout.addWidget(self.area, 3, 1, 1, 2)

        self.perimetr = QLabel(self.centralwidget)
        self.perimetr.setObjectName(u"perimetr")

        self.gridLayout.addWidget(self.perimetr, 4, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0435\u0442 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a\u043e\u0432", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0442 2:", None))
        self.fileBtn.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.Hyp.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0442 1:", None))
        self.databaseBtn.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0414", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c", None))
        self.calculateBtn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0438\u043f\u043e\u0442\u0435\u043d\u0443\u0437\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043c\u0435\u0442\u0440", None))
        self.area.setText("")
        self.perimetr.setText("")
    # retranslateUi

