from mimetypes import init
import copy
from QuestionItem import QuestionItem
from Widgets.QuestionBoolDialog import QuestionBoolDialog

__author__ = 'andrew'


class QuestionSelector:

    def __init__(self, questions_list: list):
        self.priority = 0
        self.questions_list = copy.deepcopy(questions_list)

        self.max_priority = self._find_max_priority()
        self.next_question_id = -1


    def is_end(self):
        """ @rtype: bool"""
        return not self.is_exist_questions_with_priority(self.priority)


    def select_next_question(self, next_quest_id: int):
        self.next_question_id = next_quest_id
        current_question = self._get_question_with_id(next_quest_id)
        if current_question is None:
            print("Ошибка перехода в секвенции к вопросу id[%d]" % self.next_question_id)
            return None
        self.priority = current_question.priority


    def get_next_question(self):
        """ @rtype: QuestionItem"""

        # Если был задан переход к вопросу
        if self.next_question_id >= 0:
            current_question = self._get_question_with_id(self.next_question_id)
            self.questions_list.remove(current_question)
            self.next_question_id = -1
            return current_question

        # Если нет перехода, ищем вопросы с текущим приоритетом и выбираем
        if self.is_exist_questions_with_priority(self.priority):
            current_question = self._get_question_with_priority(self.priority)
            self.questions_list.remove(current_question)
            return current_question

        return None


    def is_exist_questions_with_priority(self, arg_priorirty: int):
        """ @rtype: bool"""
        for question in self.questions_list:
            if question.priority == arg_priorirty:
                return True
        return False


    def _find_max_priority(self):
        """ @rtype: int """
        result_priority = 0
        for question in self.questions_list:
            if result_priority < question.priority:
                result_priority = question.priority
        return result_priority


    def _get_question_with_min_priority(self):
        """ @rtype: QuestionItem """
        result_priority = 999
        result_quest = None
        for question in self.questions_list:
            if result_priority > question.priority:
                result_priority = question.priority
                result_quest = question
        return result_quest


    def _get_question_with_id(self, id: int):
        """ @rtype: QuestionItem """
        for question in self.questions_list:
            if id == question.id:
                return question
        return None


    def _get_question_with_priority(self, prior: int):
        """ @rtype: QuestionItem """
        for question in self.questions_list:
            if question.priority == prior:
                return question
        return None