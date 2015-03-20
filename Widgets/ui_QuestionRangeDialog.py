# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Workspace\PyToysSelector\Widgets\QuestionRangeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QuestionRangeDialog(object):
    def setupUi(self, QuestionRangeDialog):
        QuestionRangeDialog.setObjectName("QuestionRangeDialog")
        self.gridLayout = QtWidgets.QGridLayout(QuestionRangeDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(QuestionRangeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(QuestionRangeDialog)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(QuestionRangeDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(QuestionRangeDialog)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(QuestionRangeDialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(QuestionRangeDialog)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        _translate = QtCore.QCoreApplication.translate
        QuestionRangeDialog.setWindowTitle(_translate("QuestionRangeDialog", "Вопрос"))
        self.label.setText(_translate("QuestionRangeDialog", "TextLabel"))
        self.label_2.setText(_translate("QuestionRangeDialog", "От"))
        self.label_3.setText(_translate("QuestionRangeDialog", "До"))

        self.buttonBox.accepted.connect(QuestionRangeDialog.accept)
        self.buttonBox.rejected.connect(QuestionRangeDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(QuestionRangeDialog)


