__author__ = 'andrew'

from ToyItem import ToyItem


def filter_toys(toys_list: list, filters_list: list):
    """ @rtype: list"""

    if toys_list is None or filters_list is None:
        print("Ошибка параметров фильтрации!")
        return None

    print("Фильтрация. Размер аргументов: Игрушек[%d] Фильтро-ответов[%d]" % (len(toys_list), len(filters_list)))

    result_toys = list()

    # Пробегаемся по каждой игрушке
    for toy in toys_list:

        print("Игрушка:" + toy.name)

        # Полагаем что игрушка имеет право быть в списке
        toy_validator = True

        # Пробегаемся каждым свойством по игрушке
        for property in filters_list:

            # Если у игрушки есть такое свойство
            if not property.is_suitable_for_property(toy):
                print("\tКоллизия: %s:%s"%(property.name, property.value))
                toy_validator = False
                break
            else:
                print("\tПо свойству: %s:%s"%(property.name, property.value))

        # Если все предикаты удовлетворены то добавляем игрушку в результирующий список
        if toy_validator == True:
            print("\tОдобрена!")
            result_toys.append(toy)


    return result_toys
