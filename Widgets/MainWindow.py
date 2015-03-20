from Widgets.QuestionMultiwordsDialog import QuestionMultiwordsDialog
from Widgets.ui_MainWindow import Ui_MainWindow

__author__ = 'andrew'

from PyQt5.QtWidgets import (QDialog, QPushButton, QVBoxLayout, QMessageBox, QTableWidgetItem)
from Widgets.QuestionRangeDialog import QuestionRangeDialog
from Widgets.QuestionWordDialog import QuestionWordDialog
from Widgets.QuestionBoolDialog import QuestionBoolDialog
from QuestionSelector import QuestionSelector
from Answer import Answer
from ToyProperty import ToyProperty
import ToyFilter
from Widgets.ui_MainWindow import  Ui_MainWindow


class MainWindow(QDialog):
    def __init__(self, properties_list: list, toys_list: list, questions_list: list, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow
        self.ui.setupUi(self, self)

        self.toys_list = toys_list
        self.properties_list = properties_list
        self.questions_list = questions_list

        self.answers_list = list()
        self.startSelectorButton.clicked.connect(self.on_selector_button_click);



    # Если нажата клавиша старта селектора - начинаем веселье
    def on_selector_button_click(self):

        self.toyTable.clear()

        # Создаем пустой список ответов
        self.answers_list = list()

        # Селектор вопросов
        question_selector = QuestionSelector(self.questions_list)

        # Задаем вопросы пока можно
        while not question_selector.is_end():
            # Получаем вопрос из дерева
            current_question = question_selector.get_next_question()
            if current_question is None:
                break

            # Получаем тип значений вопроса
            active_property = ToyProperty.get_property_by_name(self.properties_list, current_question.property_name)
            value_type = str(active_property.value_type).lower()

            # Для каждого типа вопроса запускам свой диалог
            if value_type == "bool":
                question_bool = QuestionBoolDialog(current_question.text)
                if question_bool.exec_():
                    print("Answer bool:" + question_bool.get_result())
                    answer = Answer(active_property.name, question_bool.get_result())
                    self.answers_list.append(answer)

            if value_type == "range":
                question_range = QuestionRangeDialog(current_question.text, 0, 100000)
                if question_range.exec_():
                    print("Answer range:" + str(question_range.get_result()))
                    answer = Answer(active_property.name, question_range.get_result())
                    self.answers_list.append(answer)

            if value_type == "word":
                question_word = QuestionWordDialog(current_question.text, active_property.values)
                if question_word.exec_():
                    print("Answer word:" + str(question_word.get_result()))
                    answer = Answer(active_property.name, question_word.get_result())
                    self.answers_list.append(answer)

            if value_type == "multiwords":
                question_multiwords = QuestionMultiwordsDialog(current_question.text, active_property.values)
                if question_multiwords.exec_():
                    print("Answer мultiwords:" + str(question_multiwords.get_result()))
                    answer = Answer(active_property.name, question_multiwords.get_result())
                    self.answers_list.append(answer)

        self.filtering()


    def filtering(self):
        # Строим список товаров подходящих под ответы
        self.answers_list = ToyFilter.filter_toys(self.toys_list, self.answers_list)

        print("\nРезультат:")
        if len(self.answers_list) == 0:
            QMessageBox.information(self, "Результат", "По данным критериям игрушек не найдено")
        else:
            for result in self.answers_list:
                print("Игрушка: [%d] %s" % (int(result.id), result.name))
            self.create_table()


    def create_table(self):
        self.toyTable.setColumnCount(3)
        self.toyTable.setRowCount(len(self.answers_list))
        header_list = ("Цена","Наименование", "Цвет")
        self.toyTable.setHorizontalHeaderLabels(header_list)

        row = 0
        for answer in self.answers_list:
            price_item = QTableWidgetItem(answer.get_property_values_in_string("Цена"))
            name_item = QTableWidgetItem(answer.name)
            self.toyTable.setItem(row, 0, price_item);
            self.toyTable.setItem(row, 1, name_item);
            row = row + 1


    def get_answer_list(self):
        return self.answers_list