from mimetypes import init
import copy
from QuestionItem import QuestionItem

__author__ = 'andrew'


class QuestionSelector:
    def __init__(self, questions_list: list):
        self.priority = 0
        self.questions_list = copy.deepcopy(questions_list)
        self.max_priority = self._find_max_priority()
        self.current_question = None

    def is_end(self):
        """ @rtype: bool"""
        if self.priority > self.max_priority:
            return True
        return False

    def get_next_question(self):
        """ @rtype: QuestionItem"""
        next_id = None

        if self.current_question is not None:
            self.priority = int(self.current_question.priority)
            next_id = self.current_question.next_question_id

            # Удаляем из списка текущий вопрос
            self.questions_list.remove(self.current_question)
        else:
            next_id = -1

        # Если текущий вопрос имел переход на другой - переходим
        if next_id is not None and next_id >= 0:
            question = self._get_question_with_id(next_id)
            if question is not None:
                self.current_question = question
                self.priority = int(question.priority)
                return self.current_question
            else:
                print("Ошибка переход к несуществующему вопросу на ID[%d]" % next_id)

        # Если нет перехода, ищем вопросы с текущим приоритетом и выбираем
        while self.is_end() == False:
            # Если есть вопросы с таким же приоритетом выбираем
            if self.is_exist_questions_with_priority(self.priority):
                self.current_question = self._get_question_with_priority(self.priority)
                break
            # Если нет вопроса с таким приоритетом - повышаем приоритет пока не больше максимума
            else:
                self.priority += 1

        if self.is_end():
            self.current_question = None

        return self.current_question

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
            if id < question.id:
                return question
        return None

    def _get_question_with_priority(self, prior: int):
        """ @rtype: QuestionItem """
        for question in self.questions_list:
            if question.priority == prior:
                return question
        return None