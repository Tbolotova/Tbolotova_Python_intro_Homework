# Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную
# сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.
#
# Пример:
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7
#
# [1, 5, 2, 3, 4, 1, 7, 8, 15, 1] => [1, 5] так как здесь есть числа от 1 до 5 и эта
# последовательность длиннее чем от 7 до 8
#
# [1, 5, 3, 4, 1, 7, 8, 15, 1] => [3, 5] так как здесь есть числа от 3 до 5 и эта
# последовательность длиннее чем от 7 до 8

from random import *


# returns a list of random values of the specified size, from 0 to the specified max value
def fill_list(el_num, max_val):
    rand_list = []
    for i in range(el_num):
        rand_list.append(randint(0, max_val))

    return rand_list


# Returns the list of a min and max values in a list of numbers
def get_min_max(numbers):
    min_value = numbers[0]
    max_value = numbers[0]
    for el in numbers:
        if el < min_value:
            min_value = el
        if el > max_value:
            max_value = el
    return min_value, max_value


# returns the max size sequence in a list of numbers, and the size of the sequence
def get_max_sequence_data(num_list, min_max_el):
    max_sequence_size = 1
    max_sequence = [min_max_el[0], min_max_el[0]]
    current_sequence_size = 1
    current_sequence = max_sequence
    for i in range(min_max_el[0], min_max_el[1]):
        if current_sequence_size == 1:
            current_sequence = [i, i]
        if i in num_list and i + 1 in num_list:
            current_sequence[1] = i + 1
            current_sequence_size += 1
            if current_sequence_size > max_sequence_size:
                max_sequence = current_sequence
                max_sequence_size = current_sequence_size
        else:
            current_sequence_size = 1
    return max_sequence, max_sequence_size


number_list = fill_list(15, 15)
min_max = get_min_max(number_list)
sequence_data = get_max_sequence_data(number_list, min_max)
if sequence_data[1] == 1:
    print(f"There are no sequential numbers in the list {number_list}")
else:
    print(f"The max sequence of numbers in the list {number_list} is {sequence_data[0]} and contains "
          f"{sequence_data[1]} elements")
