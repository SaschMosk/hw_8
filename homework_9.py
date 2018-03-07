# Список рецептов должен храниться в отдельном файле в следующем формате:
# В одном файле может быть произвольное количество блюд.
# Читать список рецептов из этого файла.
# Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных

cook_book = {
  'яйчница': [
    {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
    ],
  'стейк': [
    {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
    {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
    ],
  'салат': [
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
    {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
    {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
    ]
  }

# with open('spisok_receptov.txt', 'w') as f:
#     for dish in cook_book:
#         f.write(dish)

#
# def get_shop_list_by_dishes(dishes, person_count):
#     shop_list = {}
#     for dish in dishes:
#         for ingridient in cook_book[dish]:
#             new_shop_list_item = dict(ingridient)
#             new_shop_list_item['quantity'] *= person_count
#             if new_shop_list_item['ingridient_name'] not in shop_list:
#                 shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
#             else:
#                 shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
#     return shop_list
#
#
# def print_shop_list(shop_list):
#     for i, shop_list_item in enumerate(shop_list.values()):
#         print(i+1, '{0} {1} {2}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
#                                 shop_list_item['measure']))
#
#
# def create_shop_list():
#     person_count = int(input('Введите количество человек: '))
#     dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
#     shop_list = get_shop_list_by_dishes(dishes, person_count)
#     print_shop_list(shop_list)
#
#
# create_shop_list()


# например, сколько раз Пьер и Наташа встретились в одном абзаце в войне и мире
# count = 0
# with open('_') as f:
#    for line in f:
#        if 'Наташ' in line and 'Пьер' in line:
#            count += 1
#            print(line, end='')
# print('Наташа и Пьер упоминались вместе в {} абзацах'.format(count))

# другой пример оценки
# best_grade = None
# best_rating = None
# # извлечение классов с оценками по отдельности
# with open('scores') as f:
#     for line in f:
#         grade = line.strip()
#         scores = f.readline()
#         f.readline()
#         print('Класс {}, оценки: {}'.format(grade, scores))
#
#         int_scores = []
#         splitted = scores.split(' ')
#         for i in splitted:
#             int_scores.append(int(i))
#         average = sum(int_scores) / len(int_scores)
#         if best_rating is None or average > best_rating:
#             best_rating = average
#             best_grade = grade
# print('Лучший класс {} с лучшей оценкой: {}'.format(best_grade, best_rating))
#






#Задача 2
# json, xml, yaml форматы данных, которые имеют определенную структуру и могут использоваться разными языками программирования
# используются для обмена данными между браузером и сервером.