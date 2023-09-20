# Задача 30:
# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def get_ap(first_el, el_num, diff):
    return [first_el + (i - 1) * diff for i in range(1, el_num + 1)]


first_element = int(input("Please enter the first element of the arithmetic progression: "))
element_number = int(input("Please enter the number of elements of the progression: "))
difference = int(input("Please enter the common difference of the progression: "))
print(get_ap(first_element, element_number, difference))