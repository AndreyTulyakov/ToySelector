# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workspace\PyToysSelector\Widgets\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QHeaderView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.gridLayout = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.startSelectorButton = QtWidgets.QPushButton(MainWindow)
        self.startSelectorButton.setObjectName("startSelectorButton")
        self.verticalLayout.addWidget(self.startSelectorButton)

        self.toyTable = QtWidgets.QTableWidget(MainWindow)
        self.toyTable.setObjectName("toyTable")
        horizontHeader = self.toyTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.toyTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalLayout.addWidget(self.toyTable)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Выбор игрушки"))
        self.startSelectorButton.setText(_translate("MainWindow", "Выбрать игрушку"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

