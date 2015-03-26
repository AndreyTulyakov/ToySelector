from ConsequencesItem import ConsequencesItem

__author__ = 'andrew'

from xml.dom import minidom
from ToyProperty import ToyProperty
from ToyItem import ToyItem
from QuestionItem import QuestionItem


def load_toys_properties(properties_base_filename):
    """ @rtype: list of ToyProperty"""
    doc = minidom.parse(properties_base_filename)
    properties = doc.getElementsByTagName("property")

    result_list = list()

    for property_node in properties:
        element = ToyProperty(property_node.getAttribute("caption").lower(), property_node.getAttribute("argtype").lower())
        values = property_node.getElementsByTagName("value")
        for value in values:
            element.add_value(value.getAttribute("text").lower())
        result_list.append(element)

    return result_list


def load_toys_items(toy_base_filename, properties_list):
    """ @rtype: list of ToyItem"""
    doc = minidom.parse(toy_base_filename)
    toys_node = doc.getElementsByTagName("toy")

    toys_list = list()

    for toy_node in toys_node:
        # Загружаем в игрушку основные данные
        item = ToyItem(toy_node.getAttribute("id"), toy_node.getAttribute("name"))

        # Добавим использованные свойства из игрушки
        props_node = toy_node.getElementsByTagName("property")
        for property_node in props_node:
            prop_name = property_node.getAttribute("caption").lower()
            value = property_node.getAttribute("value").lower()

            item.add_property(prop_name, ToyProperty.get_value_type_by_property_name(properties_list, prop_name), value)

        toys_list.append(item)

    return toys_list


def load_questions(toy_questions_filename):
    """ @rtype: list of QuestionItem"""
    doc = minidom.parse(toy_questions_filename)
    questions_nodes = doc.getElementsByTagName("question")

    questions_list = list()

    for question_node in questions_nodes:

        # Загружаем в вопрос основные данные
        item = QuestionItem(
            question_node.getAttribute("id"),
            question_node.getAttribute("priority"),
            str(question_node.getElementsByTagName("text")[0].firstChild.nodeValue),
            str(question_node.getElementsByTagName("property")[0].firstChild.nodeValue.lower())
        )

        questions_list.append(item)

    return questions_list


def load_consequences(toy_consequences_filename):
    """ @rtype: list of ConsequencesItem"""
    doc = minidom.parse(toy_consequences_filename)
    questions_nodes = doc.getElementsByTagName("consequence")

    questions_list = list()

    for question_node in questions_nodes:
        # Это секвенция перехода к др вопросу?
        item = ConsequencesItem(
            str(question_node.getAttribute("if").lower()),
            str(question_node.getAttribute("then").lower())
        )
        questions_list.append(item)

    return questions_list