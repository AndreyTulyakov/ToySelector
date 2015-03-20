# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workspace\PyToysSelector\Widgets\QuestionWordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QRadioButton


class Ui_QuestionWordDialog(object):
    def setupUi(self, QuestionWordDialog):
        QuestionWordDialog.setObjectName("QuestionWordDialog")
        self.gridLayout = QtWidgets.QGridLayout(QuestionWordDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(QuestionWordDialog)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QuestionWordDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.valuesLayout = QtWidgets.QVBoxLayout()
        self.valuesLayout.setObjectName("valuesLayout")
        self.gridLayout.addLayout(self.valuesLayout, 2, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        QuestionWordDialog.setWindowTitle(_translate("QuestionWordDialog", "Вопрос"))
        self.label.setText(_translate("QuestionWordDialog", "TextLabel"))

        self.buttonBox.accepted.connect(QuestionWordDialog.accept)
        self.buttonBox.rejected.connect(QuestionWordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QuestionWordDialog)
