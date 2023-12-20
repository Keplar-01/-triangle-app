# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatabasePage.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_DataBasePage(object):
    def setupUi(self, DataBasePage):
        if not DataBasePage.objectName():
            DataBasePage.setObjectName(u"DataBasePage")
        DataBasePage.resize(320, 404)
        self.centralwidget = QWidget(DataBasePage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.cntCatet1 = QDoubleSpinBox(self.groupBox)
        self.cntCatet1.setObjectName(u"cntCatet1")
        self.cntCatet1.setMinimum(0.010000000000000)
        self.cntCatet1.setMaximum(9999.000000000000000)

        self.gridLayout_2.addWidget(self.cntCatet1, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.addRecBtn = QPushButton(self.groupBox)
        self.addRecBtn.setObjectName(u"addRecBtn")

        self.gridLayout_2.addWidget(self.addRecBtn, 4, 0, 1, 1)

        self.cntCatet2 = QDoubleSpinBox(self.groupBox)
        self.cntCatet2.setObjectName(u"cntCatet2")
        self.cntCatet2.setMinimum(0.010000000000000)
        self.cntCatet2.setMaximum(9999.000000000000000)

        self.gridLayout_2.addWidget(self.cntCatet2, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        DataBasePage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DataBasePage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 22))
        DataBasePage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DataBasePage)
        self.statusbar.setObjectName(u"statusbar")
        DataBasePage.setStatusBar(self.statusbar)

        self.retranslateUi(DataBasePage)

        QMetaObject.connectSlotsByName(DataBasePage)
    # setupUi

    def retranslateUi(self, DataBasePage):
        DataBasePage.setWindowTitle(QCoreApplication.translate("DataBasePage", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DataBasePage", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DataBasePage", u"\u041a\u0430\u0442\u0435\u0442 1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("DataBasePage", u"\u041a\u0430\u0442\u0435\u0442 2", None));
        self.groupBox.setTitle(QCoreApplication.translate("DataBasePage", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u044b\u0435 \u0441\u0442\u043e\u0440\u043e\u043d\u044b", None))
        self.label.setText(QCoreApplication.translate("DataBasePage", u"\u041a\u0430\u0442\u0435\u0442 1:", None))
        self.addRecBtn.setText(QCoreApplication.translate("DataBasePage", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("DataBasePage", u"\u041a\u0430\u0442\u0435\u0442 2:", None))
    # retranslateUi

