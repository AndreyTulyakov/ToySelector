from QuestionItem import QuestionItem
from ToyItem import ToyItem
from ToyProperty import ToyProperty

__author__ = 'andrew'


class Answer:
    def __init__(self, property_name, values):
        self.name = property_name
        self.value = values

    def is_suitable_for_property(self, toy: ToyItem):


        # Перебираем все свойства в игрушке
        for property in toy.properties_list:

            # Если имена свойств совпадают
            if self.name == property.name:

                value_type = property.value_type

                # В зависимости от типа значения используем логическое хитрое сравнение
                if value_type == "bool":
                    print("Подбор bool: Свойство %s: toyProp:%s, value:%s" % (property.name, property.values[0], self.value))
                    return property.values[0] == self.value

                if value_type == "range":
                    splitted = str(self.value).split("-")
                    min = int(splitted[0])
                    max = int(splitted[1])
                    num_value = int(property.values[0])
                    print("Подбор range: Свойство %s: min:%d, max:%d, value:%d" % (property.name, min, max, num_value))
                    if num_value >= min and num_value <= max:
                        return True
                    else:
                        return False

                if value_type == "word":
                    splitted_toy_property = str(property.values[0]).split(" ")
                    for value in splitted_toy_property:
                        if self.value == value:
                            return True
                    return False

                if value_type == "multiwords":
                    splitted = str(self.value).split(" ")
                    splitted_toy_property = str(property.values[0]).split(" ")
                    for word in splitted:
                        for value in splitted_toy_property:
                            if word == value:
                                return True
                    return False
                    pass

        # Если в игрушке нет ограничений с этим свойством то всё хорошо
        return True
