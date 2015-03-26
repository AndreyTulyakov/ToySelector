import Answer
from ConsequencesItem import ConsequencesItem

__author__ = 'andrew'

class ConsequencesChecker:

    def __init__(self):
        pass

    def single_consequence_check(self, consequnce: ConsequencesItem, answers_list: list):

        # Проход по каждому условию секвенции
        for seq_property in consequnce.if_properties:
            # Если связанных ответов вообще не было, или были иные ответы
            valud_sub = False

            # Проход по всем ответам
            for ans_property in answers_list:
                # Если условие секвенции найдено и соответсвует то считаем всё ок
                if seq_property.name == ans_property.name:

                    # Если необходим хоть какой-то ответ
                    if (seq_property.value == '*') and (ans_property.value is not None):
                        valud_sub = True

                    if seq_property.value == ans_property.value:
                        valud_sub = True

            if not valud_sub:
                return False

        # Если все условия секвенции были правдивы то секвенция годится
        return True


    def consequences_check(self, consequences_list: list, answers_list: list):
        """ @rtype: list of ConsequencesItem
            Метод возвращает список неиспользованных секвенций соответсвующий условиям списка ответов."""

        result_consequences = list()

        # Для каждой секвенции делаем проверку на удовлетворение
        for consequence in consequences_list:
            if not consequence.used:
                if self.single_consequence_check(consequence, answers_list):
                    consequence.used = True
                    result_consequences.append(consequence)

        return  result_consequences