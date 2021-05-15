
import sys
from random import randrange
import sqlite3

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QBasicTimer, QCoreApplication

from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QStackedWidget, QMessageBox, QInputDialog, QTableWidgetItem, QAction
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets

class Ui_MainWindow_ready(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playerLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playerLabel.setFont(font)
        self.playerLabel.setObjectName("playerLabel")
        self.horizontalLayout_2.addWidget(self.playerLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.readyButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.readyButton.setFont(font)
        self.readyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.readyButton.setObjectName("readyButton")
        self.gridLayout.addWidget(self.readyButton, 0, 2, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.linkorButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.linkorButton.setFont(font)
        self.linkorButton.setObjectName("linkorButton")
        self.verticalLayout_2.addWidget(self.linkorButton)
        self.kreyserButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.kreyserButton.setFont(font)
        self.kreyserButton.setObjectName("kreyserButton")
        self.verticalLayout_2.addWidget(self.kreyserButton)
        self.esminecButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.esminecButton.setFont(font)
        self.esminecButton.setObjectName("esminecButton")
        self.verticalLayout_2.addWidget(self.esminecButton)
        self.torpedButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setStrikeOut(False)
        self.torpedButton.setFont(font)
        self.torpedButton.setObjectName("torpedButton")
        self.verticalLayout_2.addWidget(self.torpedButton)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 3, 1, 1)
        self.boardMap = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.boardMap.setFont(font)
        self.boardMap.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.boardMap.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.boardMap.setObjectName("boardMap")
        self.boardMap.setColumnCount(10)
        self.boardMap.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.boardMap.setHorizontalHeaderItem(9, item)
        self.gridLayout.addWidget(self.boardMap, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.linkorImage = QtWidgets.QLabel(self.centralwidget)
        self.linkorImage.setText("")
        self.linkorImage.setObjectName("linkorImage")
        self.verticalLayout.addWidget(self.linkorImage)
        self.kreyserImage = QtWidgets.QLabel(self.centralwidget)
        self.kreyserImage.setText("")
        self.kreyserImage.setObjectName("kreyserImage")
        self.verticalLayout.addWidget(self.kreyserImage)
        self.esminecImage = QtWidgets.QLabel(self.centralwidget)
        self.esminecImage.setText("")
        self.esminecImage.setObjectName("esminecImage")
        self.verticalLayout.addWidget(self.esminecImage)
        self.torpedImage = QtWidgets.QLabel(self.centralwidget)
        self.torpedImage.setText("")
        self.torpedImage.setObjectName("torpedImage")
        self.verticalLayout.addWidget(self.torpedImage)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setProperty("intValue", 4)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_3.addWidget(self.lcdNumber)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setProperty("intValue", 3)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_3.addWidget(self.lcdNumber_2)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setProperty("intValue", 2)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout_3.addWidget(self.lcdNumber_3)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setProperty("intValue", 1)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.verticalLayout_3.addWidget(self.lcdNumber_4)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.playerLabel.setText(_translate("MainWindow", "Игрок1"))
        self.readyButton.setText(_translate("MainWindow", "Я  готов"))
        self.linkorButton.setText(_translate("MainWindow", "Поставить корабль"))
        self.kreyserButton.setText(_translate("MainWindow", "Поставить корабль"))
        self.esminecButton.setText(_translate("MainWindow", "Поставить корабль"))
        self.torpedButton.setText(_translate("MainWindow", "Поставить корабль"))
        item = self.boardMap.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.boardMap.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.boardMap.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.boardMap.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.boardMap.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.boardMap.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.boardMap.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.boardMap.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.boardMap.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.boardMap.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.boardMap.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.boardMap.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.boardMap.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.boardMap.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.boardMap.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.boardMap.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F"))
        item = self.boardMap.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "G"))
        item = self.boardMap.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "H"))
        item = self.boardMap.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "I"))
        item = self.boardMap.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "J"))
        self.label.setText(_translate("MainWindow", "Количество ячеек."))


class Ui_MainWindow_pvp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 577)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.board1Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.board1Label.setFont(font)
        self.board1Label.setObjectName("board1Label")
        self.horizontalLayout.addWidget(self.board1Label)
        self.linkorP1 = QtWidgets.QLabel(self.centralwidget)
        self.linkorP1.setText("")
        self.linkorP1.setObjectName("linkorP1")
        self.horizontalLayout.addWidget(self.linkorP1)
        self.kreyserP1 = QtWidgets.QLabel(self.centralwidget)
        self.kreyserP1.setText("")
        self.kreyserP1.setObjectName("kreyserP1")
        self.horizontalLayout.addWidget(self.kreyserP1)
        self.esminecP1 = QtWidgets.QLabel(self.centralwidget)
        self.esminecP1.setText("")
        self.esminecP1.setObjectName("esminecP1")
        self.horizontalLayout.addWidget(self.esminecP1)
        self.torpedP1 = QtWidgets.QLabel(self.centralwidget)
        self.torpedP1.setText("")
        self.torpedP1.setObjectName("torpedP1")
        self.horizontalLayout.addWidget(self.torpedP1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.linkorP2 = QtWidgets.QLabel(self.centralwidget)
        self.linkorP2.setText("")
        self.linkorP2.setObjectName("linkorP2")
        self.horizontalLayout_2.addWidget(self.linkorP2)
        self.kreyserP2 = QtWidgets.QLabel(self.centralwidget)
        self.kreyserP2.setText("")
        self.kreyserP2.setObjectName("kreyserP2")
        self.horizontalLayout_2.addWidget(self.kreyserP2)
        self.esminecP2 = QtWidgets.QLabel(self.centralwidget)
        self.esminecP2.setText("")
        self.esminecP2.setObjectName("esminecP2")
        self.horizontalLayout_2.addWidget(self.esminecP2)
        self.torpedP2 = QtWidgets.QLabel(self.centralwidget)
        self.torpedP2.setText("")
        self.torpedP2.setObjectName("torpedP2")
        self.horizontalLayout_2.addWidget(self.torpedP2)
        self.board2Label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.board2Label.setFont(font)
        self.board2Label.setObjectName("board2Label")
        self.horizontalLayout_2.addWidget(self.board2Label)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 5, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(441, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.vsLable = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Digital Counter 7")
        font.setPointSize(36)
        self.vsLable.setFont(font)
        self.vsLable.setText("")
        self.vsLable.setObjectName("vsLable")
        self.gridLayout.addWidget(self.vsLable, 0, 2, 1, 2)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(441, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(10)
        self.tableWidget_2.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        self.gridLayout.addWidget(self.tableWidget_2, 1, 3, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Game PVP"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "G"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "H"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "I"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "J"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "G"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "H"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "I"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "J"))




COORDS = {
    "A1": (0, 0),
    "A2": (1, 0),
    "A3": (2, 0),
    "A4": (3, 0),
    "A5": (4, 0),
    "A6": (5, 0),
    "A7": (6, 0),
    "A8": (7, 0),
    "A9": (8, 0),
    "A10": (9, 0),
    "B1": (0, 1),
    "B2": (1, 1),
    "B3": (2, 1),
    "B4": (3, 1),
    "B5": (4, 1),
    "B6": (5, 1),
    "B7": (6, 1),
    "B8": (7, 1),
    "B9": (8, 1),
    "B10": (9, 1),
    "C1": (0, 2),
    "C2": (1, 2),
    "C3": (2, 2),
    "C4": (3, 2),
    "C5": (4, 2),
    "C6": (5, 2),
    "C7": (6, 2),
    "C8": (7, 2),
    "C9": (8, 2),
    "C10": (9, 2),
    "D1": (0, 3),
    "D2": (1, 3),
    "D3": (2, 3),
    "D4": (3, 3),
    "D5": (4, 3),
    "D6": (5, 3),
    "D7": (6, 3),
    "D8": (7, 3),
    "D9": (8, 3),
    "D10": (9, 3),
    "E1": (0, 4),
    "E2": (1, 4),
    "E3": (2, 4),
    "E4": (3, 4),
    "E5": (4, 4),
    "E6": (5, 4),
    "E7": (6, 4),
    "E8": (7, 4),
    "E9": (8, 4),
    "E10": (9, 4),
    "F1": (0, 5),
    "F2": (1, 5),
    "F3": (2, 5),
    "F4": (3, 5),
    "F5": (4, 5),
    "F6": (5, 5),
    "F7": (6, 5),
    "F8": (7, 5),
    "F9": (8, 5),
    "F10": (9, 5),
    "G1": (0, 6),
    "G2": (1, 6),
    "G3": (2, 6),
    "G4": (3, 6),
    "G5": (4, 6),
    "G6": (5, 6),
    "G7": (6, 6),
    "G8": (7, 6),
    "G9": (8, 6),
    "G10": (9, 6),
    "H1": (0, 7),
    "H2": (1, 7),
    "H3": (2, 7),
    "H4": (3, 7),
    "H5": (4, 7),
    "H6": (5, 7),
    "H7": (6, 7),
    "H8": (7, 7),
    "H9": (8, 7),
    "H10": (9, 7),
    "I1": (0, 8),
    "I2": (1, 8),
    "I3": (2, 8),
    "I4": (3, 8),
    "I5": (4, 8),
    "I6": (5, 8),
    "I7": (6, 8),
    "I8": (7, 8),
    "I9": (8, 8),
    "I10": (9, 8),
    "J1": (0, 9),
    "J2": (1, 9),
    "J3": (2, 9),
    "J4": (3, 9),
    "J5": (4, 9),
    "J6": (5, 9),
    "J7": (6, 9),
    "J8": (7, 9),
    "J9": (8, 9),
    "J10": (9, 9),
}
players = []





def new_cell_mul():  # Когда ставлю звёздочку в QTableWidget
    cell_mul = QTableWidgetItem("*")
    cell_mul.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    return cell_mul


def new_cell_x():  # Когда ставлю крестик в QTableWidget
    cell_x = QTableWidgetItem("X")
    cell_x.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    return cell_x


def new_cell_dot():  # Когда ставлю точку в QTableWidget
    cell_dot = QTableWidgetItem(".")
    cell_dot.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
    return cell_dot



class ReadyMain(QMainWindow, Ui_MainWindow_ready):
    """Меню подготовления к самой игре"""
    
    def __init__(self, parent=None):             
        super(ReadyMain, self).__init__(parent)
        self.setupUi(self)

        self.map = SeaMap(self.boardMap)
        self.new_count()  # Обновление переменных-счётчиков
        self.new_map()  # Обновление карты


        self.initUI()

    def initUI(self):
        self.readyButton.clicked.connect(self.start)

        # Задаю цвет и форму кнопкам
        self.readyButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                       "border-radius: 10px;")
        self.linkorButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                       "border-radius: 10px;")
        self.kreyserButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                       "border-radius: 10px;")
        self.esminecButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                       "border-radius: 10px;")
        self.torpedButton.setStyleSheet("color: white; background-color: #b6afa9;"
                                       "border-radius: 10px;")


        self.linkorButton.clicked.connect(self.setLinkor)
        self.kreyserButton.clicked.connect(self.setKreyser)
        self.esminecButton.clicked.connect(self.setEsminec)
        self.torpedButton.clicked.connect(self.setTorped)


    def new_map(self):  # Метод создаёт(обновляет) карту
        for i in range(self.boardMap.columnCount()):
            for j in range(self.boardMap.rowCount()):
                self.boardMap.setItem(i, j, new_cell_dot())
        self.boardMap.resizeColumnsToContents()
        self.boardMap.resizeRowsToContents()

        self.boardMap.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.boardMap.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def new_db(self, who):  # Занесения данных в базу данных
        self.con = sqlite3.connect("Players.db")
        self.cur = self.con.cursor()
        for i, j in COORDS.items():
            self.cur.execute(f"""UPDATE {who} SET {i[0]} = '{str(self.boardMap.item(*COORDS[i]).text())}'
                         WHERE id={int(i[1:])}""")
        self.con.commit()


    def start(self):
        """Если Игрок1 нажал кнопку,
        то Игрок2 начинает заполнять данные.
        Иначе начинает игру"""
        # Проверка, все ли корабли поставлены
        if self.countL != 0 or self.countK != 0 or self.countE != 0 or self.countT != 0:
            self.error("Вы не поставили все корабли")
            return
        if self.sender().text() == 'Я  готов':
            self.new_db("Player1")
            players.append(Player('Player1', self.boardMap))  # Добавление в список игрока
            self.readyButton.setText("Я готов")
            self.playerLabel.setText("Игрок 2")
            self.new_count()  # Обновление переменных-счётчиков
            self.new_map()  # Обновление карты



        else:
            self.new_db("Player2")
            players.append(Player('Player2', self.boardMap))  # Добавление в список игрока
            windows.setCurrentIndex(1)

    def new_count(self):  # Создание(обновление) переменных-счётчиков
        self.countL = 1
        self.countK = 2
        self.countE = 3
        self.countT = 4
        self.linkorButton.setToolTip(f"{self.countL} left")
        self.kreyserButton.setToolTip(f"{self.countK} left")
        self.esminecButton.setToolTip(f"{self.countE} left")
        self.torpedButton.setToolTip(f"{self.countT} left")

    def coords_is_right(self, new_coords, num, mode='dual'):
        # проверка на правильность введённых координат
        new_coords[0] = new_coords[0].upper()
        new_coords[1] = new_coords[1].upper()
        if mode != 'v':
            return (COORDS[new_coords[1]][0] - COORDS[new_coords[0]][0] == 0 and
                    COORDS[new_coords[1]][1] - COORDS[new_coords[0]][1] == num) or \
                   (COORDS[new_coords[1]][0] - COORDS[new_coords[0]][0] == num and
                    COORDS[new_coords[1]][1] - COORDS[new_coords[0]][1] == 0)
        return (COORDS[new_coords[1]][0] - COORDS[new_coords[0]][0] == num and
                COORDS[new_coords[1]][1] - COORDS[new_coords[0]][1] == 0)

    def check(self, c1, c2, i, num):
        # Проверка, если в координатах есть * или X,
        if num == 1:
            return (str(self.boardMap.item(c1 + i, c2).text()) == "*" or
                    str(self.boardMap.item(c1 + i, c2).text()) == "X")
        return (str(self.boardMap.item(c1, c2 + i).text()) == "*" or
                str(self.boardMap.item(c1, c2 + i).text()) == "X")

    def error(self, text="Вы неправильно ввели координаты."):  # Вызов ошибки
        QMessageBox.critical(self, 'Ошибка!', text)

    def setShip(self, coords, num, who):  # Создание любого корабля на поле
        error = False
        new_coords = coords.split('-')
        if self.coords_is_right(new_coords, num):
            if self.coords_is_right(new_coords, num, 'v'):
                vertical = True
            else:
                vertical = False
            c1, c2 = COORDS[new_coords[0]][0], COORDS[new_coords[0]][1]
            for i in range(num + 1):
                if not vertical:
                    if self.check(c1, c2, i, 2):
                        error = True
                        self.error()
                        break
                    self.boardMap.setItem(c1, c2 + i, new_cell_x())
                    if i == num:
                        self.map.shoot(c1, c2 + i, "sink")
                else:
                    if self.check(c1, c2, i, 1):
                        error = True
                        self.error()
                        break
                    self.boardMap.setItem(c1 + i, c2, new_cell_x())
                    if i == num:
                        self.map.shoot(c1 + i, c2, 'sink')
            if not error:
                if who == "L":
                    self.countL -= 1
                    self.linkorButton.setToolTip(f"{self.countL} left")
                elif who == "K":
                    self.countK -= 1
                    self.kreyserButton.setToolTip(f"{self.countK} left")
                elif who == "E":
                    self.countE -= 1
                    self.esminecButton.setToolTip(f"{self.countE} left")
        else:
            self.error()



    def setLinkor(self):  # Создание Линкора
        if self.countL == 0:
            self.error("Все корабли поставлены")
            return
        coords, ok = QInputDialog.getText(self, f'Линкор', 'Введите координаты для Линкора:\n'
                                                                       'Например: A1-D1')
        if ok and self.countL != 0:
            try:
                self.setShip(coords, 3, "L")
            except BaseException:
                self.error()

    def setKreyser(self):  # Создание Крейсера
        if self.countK == 0:
            self.error("Все корабли поставлены")
            return
        coords, ok = QInputDialog.getText(self, f'Крейсер', 'Введите координаты для Крейсера:\n'
                                                                       'Например: A3-C3')
        if ok and self.countK != 0:
            try:
                self.setShip(coords, 2, "K")
            except BaseException:
                self.error()

    def setEsminec(self):  # Создание Эсминца
        if self.countE == 0:
            self.error("Все корабли поставлены")
            return
        coords, ok = QInputDialog.getText(self, f'Эсминец', 'Введите координаты для Эсминца:\n'
                                                                       'Например: A5-B5')
        if ok and self.countE != 0:
            try:
                self.setShip(coords, 1, "E")
            except BaseException:
                self.error()

    def setTorped(self):  # Создание торпедной лодки
        if self.countT == 0:
            self.error("Все корабли поставлены")
            return
        coord, ok = QInputDialog.getText(self, f'Торпеда', 'Введите координаты для Торпеды:\n'
                                                                      'Например: A7')
        if ok and self.countT != 0:
            try:
                if str(self.boardMap.item(*COORDS[coord.upper()]).text()) == ".":
                    self.boardMap.setItem(*COORDS[coord.upper()], new_cell_x())
                    self.map.shoot(*COORDS[coord.upper()], 'sink')
                    self.countT -= 1
                    self.torpedButton.setToolTip(f"{self.countT} left")
                else:
                    self.error()
            except BaseException:
                self.error()


class PVPMain(QMainWindow, Ui_MainWindow_pvp):
    def __init__(self, parent=None):
        super(PVPMain, self).__init__(parent)
        self.setupUi(self)


        self.turn = "Игрок1"  # Очередь первого игрока


        self.map1 = SeaMap(self.tableWidget)
        self.map2 = SeaMap(self.tableWidget_2)

        self.new_boards()  # Создание игрового поля

        self.initUI()

    def initUI(self):
        self.tableWidget.cellClicked[int, int].connect(self.course1)
        self.tableWidget_2.cellClicked[int, int].connect(self.course2)


        self.board1Label.setText("Игрок 1")
        self.board2Label.setText("Игрок 2")
        self.board1Label.setStyleSheet("background-color: #B22222")
        self.board2Label.setStyleSheet("background-color: #1E90FF")


        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)


        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.tableWidget_2.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def new_boards(self):
        for i in range(self.tableWidget.columnCount()):
            for j in range(self.tableWidget.rowCount()):
                self.tableWidget.setItem(i, j, new_cell_dot())
        for i in range(self.tableWidget_2.columnCount()):
            for j in range(self.tableWidget_2.rowCount()):
                self.tableWidget_2.setItem(i, j, new_cell_dot())
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.resizeRowsToContents()

    def change_of_course(self):  # Смена хода
        if self.turn == "Игрок1":
            self.turn = "Игрок2"
            self.board1Label.setText("Игрок 1")
            self.board2Label.setText("Игрок 2")
            self.board1Label.setStyleSheet("background-color: #B22222")
            self.board2Label.setStyleSheet("background-color: #1E90FF")
            players[0], players[1] = players[1], players[0]
        elif self.turn == "Игрок2":
            self.turn = "Игрок1"
            self.board1Label.setText("Игрок 1")
            self.board2Label.setText("Игрок 2")
            self.board1Label.setStyleSheet("background-color: #B22222")
            self.board2Label.setStyleSheet("background-color: #1E90FF")
            players[0], players[1] = players[1], players[0]


    def info(self, text="Координаты правельные"):  # Информационное табло
        QMessageBox.information(self, "INFO", text)

    def error(self, text="Вы уже стреляли в эту клетку."):  # Вызов ошибки
        QMessageBox.critical(self, 'Ошибка!', text)

    def check(self):
        if all(players[1].board[i][j] == 0 for i in range(10) for j in range(10)):
            self.info(f"Выиграл {self.turn}!")
            windows.setCurrentIndex(5)
            return

    def course1(self, c1, c2):
        self.course(c1, c2, 1)

    def course2(self, c1, c2):
        self.course(c1, c2, 2)

    def course(self, r, c, num):  # Ход
        if self.turn[-1] == '1' and num == 2 or self.turn[-1] == '2' and num == 1:
            flag = True
            coord = (r, c)
        else:
            flag = False

        if num == 1:
            if str(self.tableWidget.item(r, c).text()) == "*" or str(self.tableWidget.item(r, c).text()) == "X" :
                self.error()
                return
        else:
            if str(self.tableWidget_2.item(r, c).text()) == "*" or str(self.tableWidget_2.item(r, c).text()) == "X" :
                self.error()
                return

        if flag:
            if self.dot_or_notdot((r, c)):
                if any(self.hasOne((r, c), shift)
                       for shift in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                    self.info("Попадание!")
                    if self.turn[-1] == '1':
                        self.map2.shoot(r, c, 'hit')
                    else:
                        self.map1.shoot(r, c, 'hit') 
                    players[1].board[r][c] = 0

                else:
                    self.info("Корабль потоплен!")
                    if self.turn[-1] == '1':
                        self.map2.shoot(r, c, 'sink')
                    else:
                        self.map1.shoot(r, c, 'sink')
                    players[1].board[r][c] = 0

                    self.check()
            else:
                self.info("Промах!")
                if self.turn[-1] == '1':
                    self.map2.shoot(r, c, 'miss')
                else:
                    self.map1.shoot(r, c, 'miss')

                self.change_of_course()
        else:
            QMessageBox.critical(self, "Ошибка!", "Не ваша очередь!")

    def dot_or_notdot(self, coord):  # Проверка попал, не попал
        new_coord = None
        for key, value in COORDS.items():
            if value == coord:
                new_coord = (key, value)
                break
        con = sqlite3.connect("Players.db")
        cur = con.cursor()
        result = cur.execute(
            f"""SELECT {new_coord[0][0]} FROM Player{players[1].who[-1]}
            WHERE id={new_coord[1][0] + 1}""").fetchone()
        if result[0] == "." or result[0] == "*":
            return False
        return True

    def hasOne(self, pos, shift):  # Проверка, потопил или ранил
        x, y = pos
        dx, dy = shift
        x += dx
        y += dy
        if 0 <= x < 10 and 0 <= y < 10:
            if players[1].board[x][y] == 1:
                if players[1].board[x-1][y-1] == 0:
                    if players[1].board[x+1][y+1] == 0:
                        if players[1].board[x-1][y] == 0:
                            return True
        return False




class Player:
    def __init__(self, who, map):
        self.who = who
        self.board = []
        for i in range(10):
            self.board.append([])
            for j in range(10):
                self.board[i].append(0)
        for i in range(10):
            for j in range(10):
                if str(map.item(i, j).text()) == 'X':
                    self.board[i][j] = 1


class SeaMap:
    def __init__(self, board):
        self.map = board

    def shoot(self, row, col, result):
        if result == 'miss':
            self.map.setItem(row, col, new_cell_mul())
        elif result == 'hit':
            self.map.setItem(row, col, new_cell_x())
        elif result == 'sink':
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        if str(self.map.item(i, j).text()) == '.':
                            self.map.setItem(i, j, new_cell_mul())
            self.map.setItem(row, col, new_cell_x())
            for j in range(10):
                if str(self.map.item(row, j).text()) == 'X':
                    col = j
                    for i in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= i < 10 and 0 <= u < 10:
                                if str(self.map.item(i, u).text()) == '.':
                                    self.map.setItem(i, u, new_cell_mul())
            for v in range(10):
                if str(self.map.item(v, col).text()) == 'X':
                    row = v
                    for v in range(row - 1, row + 2):
                        for u in range(col - 1, col + 2):
                            if 0 <= v < 10 and 0 <= u < 10:
                                if str(self.map.item(v, u).text()) == '.':
                                    self.map.setItem(v, u, new_cell_mul())


if __name__ == '__main__': 
    app = QApplication(sys.argv)

   
    ready_window = ReadyMain()
    pvp_window = PVPMain()

    windows = QStackedWidget()


    windows.addWidget(ready_window)  # 0
    windows.addWidget(pvp_window)  # 1


    windows.setWindowTitle("Морской бой")
    windows.show()
    sys.exit(app.exec())
