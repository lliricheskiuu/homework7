import random as rnd

# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

# 1.

my_list = [rnd.randint(1, 100) for value in range(1, 20)]
print(my_list)

# 2.

my_list = []

for value in range(1, 20):
    my_list.append(rnd.randint(1, 100))

print(my_list)

###

# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом
# с помощью модуля random в диапазоне от -10 до 10 по каждой оси.


def create_random_point():
    point = (rnd.randint(-10, 10),
             rnd.randint(-10, 10),
             rnd.randint(-10, 10))
    return point


triangle = {"A": create_random_point(),
            "B": create_random_point(),
            "C": create_random_point()}

print(triangle)

###

# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***


def my_print(string):
    string = "***" + string + "***"
    return string


my_str = str(input("Enter your string:"))
print(my_print(my_str))

###

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
# попытка без интернета: (неуспешная)
# persons = [{"name": "John", "age": 15},
# {"name": "Jack", "age": 45},
# {"name": "Max", "age": 10},
# {"name": "Kirill", "age": 25},
# {"name": "Damir", "age": 10}]

# names = []
# i = 0
# min_age = my_list[i]["age"]
#
# for i in range(len(my_list)):
#     if my_list[i]["age"] <= min_age:
#         min_age = my_list[i]["age"]
#         names.clear()
#         names.append(my_list[i]["name"])
#     i += 1
#
# print("The youngest:", ', '.join(names))

from collections import defaultdict

persons = [
    {"name": "Yugo", "age": 27},
    {"name": "Norman", "age": 12},
    {"name": "Emma", "age": 12},
    {"name": "Ray", "age": 12}
]

age_by_names = defaultdict(list)
len_name_by_names = defaultdict(list)
ages = []

for i in persons:
    name = i['name']
    age = i['age']
    age_by_names[age].append(name)
    len_name_by_names[len(name)].append(name)
    ages.append(age)

# print("\n")
# print(age_by_names)
# print(len_name_by_names, "\n")

# а)

min_age = min(age_by_names)
print('The youngest:', age_by_names[min_age])

# б)

max_len_name = max(len_name_by_names)
if len(len_name_by_names[max_len_name]) > 1:
    print('The longest names:', len_name_by_names[max_len_name])
else:
    print('The longest name:', len_name_by_names[max_len_name])

# в)

print('Average age:', sum(ages) // len(ages))

###

# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {1: "q", 2: "w", 3: "e", 4: "r", 5: "t"}
my_dict_2 = {2: "q", 7: "u", 21: "l", 4: "j", 5: "b"}

my_list_1 = []

set_dict_1 = set(my_dict_1)
set_dict_2 = set(my_dict_2)

# а)

for key in set_dict_1.intersection(set_dict_2):
    my_list_1.append(key)
print(my_list_1)

# б)

my_list_2 = []

for key in set_dict_1:
    if list(my_dict_2).count(key) == 0:
        my_list_2.append(key)
print(my_list_2)

# в)

res_dict_1 = {}

for key, value in my_dict_1.items():
    if list(my_dict_2).count(key) == 0:
        res_dict_1[key] = value
print(res_dict_1)

# г)

res_dict_2 = {}

for key, value in my_dict_1.items():
    if list(my_dict_2).count(key) == 0:
        res_dict_2[key] = value

for key, value in my_dict_2.items():
    if list(my_dict_1).count(key) == 0:
        res_dict_2[key] = value

for key in set_dict_1.intersection(set_dict_2):
    res_dict_2[key] = my_dict_1[key], my_dict_2[key]

print(res_dict_2)