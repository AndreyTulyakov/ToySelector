__author__ = 'andrew'

# from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QCheckBox
from Widgets.ui_QuestionMultiwordsDialog import Ui_QuestionMultiwordsDialog


class QuestionMultiwordsDialog(QDialog):
    def __init__(self, textQuestion: str, arg_values: list, parent=None):
        super(QuestionMultiwordsDialog, self).__init__(parent)

        self.ui = Ui_QuestionMultiwordsDialog
        self.ui.setupUi(self, self)
        self.label.setText(textQuestion)

        self.values_count = len(arg_values)
        self.arg_values = arg_values
        self.value_widgets = list()

        self._init_values_widgets()



    def _init_values_widgets(self):
        for value in self.arg_values:
            radioButton =  QCheckBox(self)
            radioButton.setText(value)
            self.valuesLayout.addWidget(radioButton)
            self.value_widgets.append(radioButton)


    def get_result(self):
        """ @rtype: str """
        result = ""
        for checkbox in self.value_widgets:
            if checkbox.isChecked():
                result = str.format("%s %s" % (result, checkbox.text()))
        # Удалим первый пробел
        if len(result) > 0 and result[0] == ' ':
            result = result[1:]
        return result
