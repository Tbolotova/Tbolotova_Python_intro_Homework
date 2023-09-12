# задача 1 необязательная.
# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты
# случайные от -10 до 10.
#
# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

from random import *
from math import *


def get_multipliers(max_pow):
    pow_multipliers = dict()
    for i in range(max_pow, -1, -1):
        pow_multipliers[i] = randint(-10, 10)
    return pow_multipliers


def get_polynomial(pow_multiplier_dict, max_power):
    polynomial = ''
    for key, value in pow_multiplier_dict.items():
        sign = ''
        x_part = ''
        if value < 0:
            sign = ('- ' if key == max_power else ' - ')
        elif value > 0:
            sign = ('' if key == max_power else ' + ')
        if abs(key) > 1:
            x_part = f'x ^ {key}'
        elif key == 1:
            x_part = 'x'
        if abs(value) > 1:
            polynomial += f'{sign}{abs(value)}{x_part}'
        elif abs(value) == 1:
            polynomial += f'{sign}{x_part}'
    return polynomial


k = int(input("Please enter an integer: "))
pow_multiplier_d = get_multipliers(k)
print(pow_multiplier_d)
print(get_polynomial(pow_multiplier_d, k) + ' = 0')
