from ConsequencesItem import ConsequencesItem

__author__ = 'andrey tulyakov'
import sys

from PyQt5.QtWidgets import QApplication

import ToysBaseLoader
from Widgets.MainWindow import MainWindow


program_version = 0.01

toy_properties_base_filename = "XmlBase/ToysProperties.xml"
toy_items_base_filename = "XmlBase/Toys.xml"
toy_questions_filename = "XmlBase/Questions.xml"
toy_consequences_filename = "XmlBase/Consequences.xml"

def main():

    print('Программа для выбора игрушки. Версия:', program_version)

    print('Загрузка свойств...')
    properties_list = ToysBaseLoader.load_toys_properties(toy_properties_base_filename)

    print('Загрузка игрушек...')
    toys_list = ToysBaseLoader.load_toys_items(toy_items_base_filename, properties_list)

    print('Загрузка вопросов...')
    questions_list = ToysBaseLoader.load_questions(toy_questions_filename)

    print('Загрузка условных секвенций...')
    consequences_list = ToysBaseLoader.load_consequences(toy_consequences_filename)

    for cons in consequences_list:
        print("if:")
        for uslo in cons.if_properties:
            print("\t%s:%s"%(uslo.name, uslo.value))

        print("then:")
        if cons.is_goto:
            print("\tnext ID:%d"%cons.next_question_id)
        else:
            for uslo in cons.then_properties:
                print("\t%s:%s"%(uslo.name, uslo.value))

    #for prop in properties_list:
    #    print("Свойство:%s тип:%s" % (prop.name, prop.value_type))

    app = QApplication(sys.argv)
    start_dialog = MainWindow(properties_list, toys_list, questions_list, consequences_list)
    start_dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
