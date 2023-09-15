# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно
#
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]
from random import *


def set_list(size):
    return [randint(-100, 100) for i in range(size)]


def get_indexes_in_range(init_list, min_val, max_val):
    return [i for i in range(len(init_list) - 1) if min_val <= init_list[i] <= max_val]


list_size = int(input("Please enter the list size: "))
min_value = int(input("Please enter the min value: "))
max_value = int(input("Please enter the max value: "))
initial_list = set_list(list_size)
print(f"In the list {initial_list} the following indexes are in the range between {min_value} "
      f"and {max_value} (inclusive): {get_indexes_in_range(initial_list, min_value, max_value)}")
