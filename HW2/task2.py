# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math
import random


def get_numbers(num_sum, product):
    numbers_calc = []
    discriminant = num_sum * num_sum - 4 * product
    first_num_calc = int((num_sum + math.sqrt(discriminant)) / 2)
    numbers_calc.append(first_num_calc)
    second_num_calc = num_sum - first_num_calc
    numbers_calc.append(second_num_calc)
    return numbers_calc


def check_numbers(numbers_found, first_number_set, second_number_set):
    if numbers_found[0] == first_number_set or numbers_found[0] == second_number_set:
        print(f"The first number {numbers_found[0]} has been guessed correctly")
    else:
        print("The numbers were guessed incorrectly. Try again.")
    if numbers_found[1] == first_number_set or numbers_found[1] == second_number_set:
        print(f"The second number {numbers_found[1]} has been guessed correctly")
    else:
        print("The numbers were guessed incorrectly. Try again.")


first_num = random.randrange(1, 1000)
second_num = random.randrange(1, 1000)
s = first_num + second_num
print(f"The sum of the numbers is {s}")
p = first_num * second_num
print(f"The product of the numbers multiplication is {p}")
numbers = get_numbers(s, p)
print(f"The numbers are {numbers}")
check_numbers(numbers, first_num, second_num)
