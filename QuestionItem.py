__author__ = 'andrew'

class QuestionItem:

    def __init__(self, arg_id: int, priority: int, text: str, property_name: str):
        self.id = int(arg_id)
        self.priority = int(priority)
        self.text = text
        self.property_name = str(property_name)

    pass