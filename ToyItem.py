import ToyProperty

__author__ = 'andrew'

from ToyProperty import ToyProperty

class ToyItem:

    def __init__(self, arg_id, name):
        self.id = arg_id
        self.name = name
        self.properties_list = list()

    def add_property(self, name: str, value_type: str, value):
        prop = ToyProperty(name, value_type)
        prop.add_value(value)
        self.properties_list.append(prop)

    def is_contain_property(self, property_name: str):
        """ @rtype: bool """
        for prop in self.properties_list:
            if prop.name == property_name:
                return True
        return False

    def is_property_contain_value(self, property_name: str, value):
        """ @rtype: bool """
        for prop in self.properties_list:
            if prop.name == property_name:
                for val in prop.values:
                    if val == value:
                        return True
        return False

    def get_property_values(self, property_name):
        for prop in self.properties_list:
            if prop.name == property_name:
                return  prop.values
        return None

    def get_property_values_in_string(self, property_name):
        for prop in self.properties_list:
            if prop.name == property_name:
                result = ""
                for val in prop.values:
                    result = str.format("%s %s"%(result, val))
                return  result[1:]
        return None