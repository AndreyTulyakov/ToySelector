from ConsequencesChecker import ConsequencesChecker
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
    def __init__(self,
                 properties_list: list, toys_list: list, questions_list: list, consequences_list:list, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow
        self.ui.setupUi(self, self)

        self.toys_list = toys_list
        self.properties_list = properties_list
        self.questions_list = questions_list
        self.consequences_list = consequences_list

        self.answers_list = list()
        self.startSelectorButton.clicked.connect(self.on_selector_button_click);



    # Если нажата клавиша старта селектора - начинаем веселье
    def on_selector_button_click(self):

        self.toyTable.clear()

        # Создаем пустой список ответов
        self.answers_list = list()

        # Селектор вопросов
        question_selector = QuestionSelector(self.questions_list)
        consequences_checker = ConsequencesChecker();

        # Задаем вопросы пока можно
        while True:
            # Получаем вопрос из дерева
            current_question = question_selector.get_next_question()
            if current_question is None:
                break

            # Получаем тип значений вопроса
            active_property = ToyProperty.get_property_by_name(self.properties_list, current_question.property_name)
            value_type = str(active_property.value_type).lower()

            answer = None

            # Для каждого типа вопроса запускаем свой диалог
            if value_type == "bool":
                question_bool = QuestionBoolDialog(current_question.text)
                if question_bool.exec_():
                    answer = Answer(active_property.name, question_bool.get_result())
                    self.answers_list.append(answer)

            if value_type == "range":
                question_range = QuestionRangeDialog(current_question.text, 0, 100000)
                if question_range.exec_():
                    answer = Answer(active_property.name, question_range.get_result())
                    self.answers_list.append(answer)

            if value_type == "word":
                question_word = QuestionWordDialog(current_question.text, active_property.values)
                if question_word.exec_():
                    answer = Answer(active_property.name, question_word.get_result())
                    self.answers_list.append(answer)

            if value_type == "multiwords":
                question_multiwords = QuestionMultiwordsDialog(current_question.text, active_property.values)
                if question_multiwords.exec_():
                    if question_multiwords.get_result() is not None:
                        answer = Answer(active_property.name, question_multiwords.get_result())
                        self.answers_list.append(answer)

            # Если ответ НЕ был отказом, то просматриваем секвенции и получаем список с валидными условиями
            if answer is not None:
                list_of_used_consequences = consequences_checker.consequences_check(
                    self.consequences_list, self.answers_list
                )
                print("# list_of_used_consequences size:%d"%len(list_of_used_consequences))
                # Необходимо удовлетворить каждую условную секвенцию из списка
                for used_consequence in list_of_used_consequences:

                    # Если это вопросный переход
                    if used_consequence.is_goto:
                        print("Sequence GOTO:%d" % used_consequence.next_question_id)
                        question_selector.select_next_question(used_consequence.next_question_id)
                    # Если это задача присваивания
                    else:
                        for then_prop in used_consequence.then_properties:
                            print("Sequence SET: [%s:%s]" %(then_prop.name, then_prop.value))
                            finded = False
                            for ans in self.answers_list:
                                if ans.name == then_prop.name:
                                    ans.value = then_prop.value
                                    finded = True

                            if not finded:
                                self.answers_list.append(Answer(then_prop.name, then_prop.value))

        self.filtering()


    def filtering(self):
        # Строим список товаров подходящих под ответы
        self.answers_list = ToyFilter.filter_toys(self.toys_list, self.answers_list)

        print("\nРезультат:")
        if len(self.answers_list) == 0:
            QMessageBox.information(self, "Результат", "По данным критериям игрушек не найдено")
        else:
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