__author__ = 'andrew'

#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QRadioButton

from Widgets.ui_QuestionWordDialog import Ui_QuestionWordDialog


class QuestionWordDialog(QDialog):

    def __init__(self, textQuestion: str, arg_values: list, parent = None):
        super(QuestionWordDialog, self).__init__(parent)

        self.ui = Ui_QuestionWordDialog
        self.ui.setupUi(self, self)
        self.label.setText(textQuestion)

        self.values_count = len(arg_values)
        self.arg_values = arg_values
        self.value_widgets = list()

        self._init_values_widgets()



    def _init_values_widgets(self):
        for value in self.arg_values:
            radioButton =  QRadioButton(self)
            radioButton.setText(value)
            self.valuesLayout.addWidget(radioButton)
            self.value_widgets.append(radioButton)

        if len(self.value_widgets) > 0:
            self.value_widgets[0].setChecked(True)


    def get_result(self):
        """ @rtype: str """
        result = ""
        for radioButton in self.value_widgets:
            if radioButton.isChecked():
                result += radioButton.text()

        return result
