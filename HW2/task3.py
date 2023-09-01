# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

import math


def power_of_two(max_num):
    power = 0
    pow_two = []
    while math.pow(2, power) < max_num:
        pow_two.append(int(math.pow(2, power)))
        power += 1

    return pow_two


max_number = int(input("Please enter the max number: "))
print(f"The powers of 2 up to {max_number} are: {power_of_two(max_number)}")
