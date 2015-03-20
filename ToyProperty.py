__author__ = 'andrew'

class ToyProperty:

    def __init__(self, name, value_type):
        self.name = name
        self.value_type = value_type
        self.values = list()
        if self.value_type == "bool":
            self.values.append("0")
            self.values.append("1")

    def is_contain_value(self, value):
        for element in self.values:
            if element == value:
                return True
        return False

    def is_contain_value_by_name(self, value):
        for element in self.values:
            if element == value:
                return True
        return False

    def add_value(self, value):
        if(self.is_contain_value(value) == False):
            self.values.append(value)

    @staticmethod
    def properties_is_exist(properties_list, name):
        for prop in properties_list:
            if(prop.name == name):
                return True
        return False

    @staticmethod
    def get_property_by_name(properties_list, name):
        """ @rtype ToyProperty """
        for prop in properties_list:
            if(prop.name == name):
                return prop
        return None

    @staticmethod
    def get_value_type_by_property_name(properties_list, name):
        for prop in properties_list:
            if(prop.name == name):
                return prop.value_type
        return None
