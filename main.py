__author__ = 'andrey tulyakov'
import sys

from PyQt5.QtWidgets import QApplication

import ToysBaseLoader
from Widgets.MainWindow import MainWindow


program_version = 0.01

toy_properties_base_filename = "XmlBase/ToysProperties.xml"
toy_items_base_filename = "XmlBase/Toys.xml"
toy_questions_filename = "XmlBase/Questions.xml"


def main():

    print('Программа для выбора игрушки. Версия:', program_version)

    print('Загрузка свойств...')
    properties_list = ToysBaseLoader.load_toys_properties(toy_properties_base_filename)

    print('Загрузка игрушек...')
    toys_list = ToysBaseLoader.load_toys_items(toy_items_base_filename, properties_list)

    print('Загрузка вопросов...')
    questions_list = ToysBaseLoader.load_questions(toy_questions_filename)

    #for prop in properties_list:
    #    print("Свойство:%s тип:%s" % (prop.name, prop.value_type))

    app = QApplication(sys.argv)
    start_dialog = MainWindow(properties_list, toys_list, questions_list)
    start_dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
