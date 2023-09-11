# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def get_num_from_2_lists(input_lists):
    input_lists[0] = set(input_lists[0])
    input_lists[1] = set(input_lists[1])
    matching_num_list = []
    for item in input_lists[0]:
        if item in input_lists[1]:
            matching_num_list.append(item)
    matching_num_list.sort()
    return matching_num_list


def input_num():
    list_size = [int(input("Please enter the size of the first list: ")),
                 int(input("Please enter the size of the second list: "))]
    lists = [[], []]
    for i in range(len(list_size)):
        curr_el = 0
        while curr_el < list_size[i]:
            lists[i].append(input("Please enter a number: "))
            curr_el += 1
    return lists


print(get_num_from_2_lists(input_num()))
