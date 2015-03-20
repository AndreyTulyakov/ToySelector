__author__ = 'andrew'

#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Widgets.ui_QuestionRangeDialog import Ui_QuestionRangeDialog

class QuestionRangeDialog(QDialog):
    def __init__(self, textQuestion: str, min:int, max:int, parent = None):
        super(QuestionRangeDialog, self).__init__(parent)

        self.ui = Ui_QuestionRangeDialog
        self.ui.setupUi(self, self)
        self.label.setText(textQuestion)

        self.spinBox.setMinimum(min)
        self.spinBox.setMaximum(max)

        self.spinBox_2.setMinimum(min)
        self.spinBox_2.setMaximum(max)

    def get_result(self):
        """ @rtype: str """
        result = str.format("%d-%d" % (self.spinBox.value(), self.spinBox_2.value()))
        return result
