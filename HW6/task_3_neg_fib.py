# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# для k = 8 список будет выглядеть так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

from math import *


# Я очень хотела спать, и мне ничего не приходило в голову, кроме аппроксимации)
# Мне даже понравилось это решение) Такой себе милый способ обмануть систему. Ниже есть нормальное решение))
# F(n) ≈ (golden_ratio ^ n + (1 - golden_ratio) ^ n) / √5
def neg_fib_golden_ratio(el_num):
    golden_ratio = 1.618034
    return [-round((golden_ratio ** i + (1 - golden_ratio) ** i)/sqrt(5)) if i < 0
            else round((golden_ratio ** i + (1 - golden_ratio) ** i)/sqrt(5)) for i in range(-el_num, el_num + 1)]


def get_fib_el(index):
    if abs(index) == 0:
        return 0
    if abs(index) == 1:
        return 1
    if index > 0:
        return get_fib_el(index - 1) + get_fib_el(index - 2)
    if index < 0:
        return int((-1)**(index + 1) * (get_fib_el(abs(index) - 1) + get_fib_el(abs(index) - 2)))


k = 8
print([get_fib_el(i) for i in range(-k, k + 1)])
print(neg_fib_golden_ratio(k))
