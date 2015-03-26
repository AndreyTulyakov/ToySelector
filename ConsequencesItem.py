__author__ = 'andrew'

from Answer import Answer


class ConsequencesItem:
    def __init__(self, ifvalue: str, thenvalue):

        self.used = False
        ifvalue = ifvalue.lower()
        thenvalue = thenvalue.lower()

        self.if_properties = list()
        self.then_properties = list()

        # Если несколько условий соединённых ' and ' то распределяем в список Answer'ов
        ifvalues = ifvalue.split(" and ")
        for ivalue in ifvalues:
            full_arg = ivalue.split(":")
            self.if_properties.append(Answer(full_arg[0], full_arg[1]))

        then_values = thenvalue.split("; ")
        for then_value in then_values:
            full_arg = then_value.split(":")
            self.then_properties.append(Answer(full_arg[0], full_arg[1]))

