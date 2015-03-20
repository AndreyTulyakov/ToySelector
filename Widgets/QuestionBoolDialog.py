__author__ = 'andrew'

# from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Widgets.ui_QuestionBoolDialog import Ui_QuestionBoolDialog


class QuestionBoolDialog(QDialog):
    def __init__(self, textQuestion: str, parent=None):
        super(QuestionBoolDialog, self).__init__(parent)

        self.ui = Ui_QuestionBoolDialog
        self.ui.setupUi(self, self)
        self.label.setText(textQuestion)

    def get_result(self):
        """ @rtype: str """
        if self.radioButtonYes.isChecked():
            return "1"
        else:
            return "0"
