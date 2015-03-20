# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workspace\PyToysSelector\Widgets\QuestionMultiwordsDialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QuestionMultiwordsDialog(object):
    def setupUi(self, QuestionMultiwordsDialog):
        QuestionMultiwordsDialog.setObjectName("QuestionMultiwordsDialog")
        self.gridLayout = QtWidgets.QGridLayout(QuestionMultiwordsDialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(QuestionMultiwordsDialog)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(QuestionMultiwordsDialog)
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
        QuestionMultiwordsDialog.setWindowTitle(_translate("QuestionMultiwordsDialog", "Вопрос"))
        self.label.setText(_translate("QuestionMultiwordsDialog", "TextLabel"))

        self.buttonBox.accepted.connect(QuestionMultiwordsDialog.accept)
        self.buttonBox.rejected.connect(QuestionMultiwordsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QuestionMultiwordsDialog)
