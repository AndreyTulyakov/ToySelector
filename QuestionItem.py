__author__ = 'andrew'

class QuestionItem:

    def __init__(self, arg_id: int, priority: int, text: str, property_name: str, next_question_id: int):
        self.id = int(arg_id)
        self.priority = int(priority)
        self.text = text
        self.property_name = str(property_name)
        self.next_question_id = next_question_id

    pass