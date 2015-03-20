# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workspace\PyToysSelector\Widgets\QuestionBoolDialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuestionBoolDialog(object):
    def setupUi(self, questionBoolDialog):
        questionBoolDialog.setObjectName("QuestionBoolDialog")
        self.gridLayout = QtWidgets.QGridLayout(questionBoolDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(questionBoolDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(questionBoolDialog)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.radioButtonYes = QtWidgets.QRadioButton(questionBoolDialog)
        self.radioButtonYes.setObjectName("radioButtonYes")
        self.gridLayout.addWidget(self.radioButtonYes, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.radioButtonNo = QtWidgets.QRadioButton(questionBoolDialog)
        self.radioButtonNo.setObjectName("radioButtonNo")
        self.gridLayout.addWidget(self.radioButtonNo, 3, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        questionBoolDialog.setWindowTitle(_translate("QuestionBoolDialog", "Вопрос"))
        self.label.setText(_translate("QuestionBoolDialog", "Вопрос"))
        self.radioButtonYes.setText(_translate("QuestionBoolDialog", "Да"))
        self.radioButtonNo.setText(_translate("QuestionBoolDialog", "Нет"))
        self.radioButtonYes.setChecked(True)

        self.buttonBox.accepted.connect(questionBoolDialog.accept)
        self.buttonBox.rejected.connect(questionBoolDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(questionBoolDialog)
