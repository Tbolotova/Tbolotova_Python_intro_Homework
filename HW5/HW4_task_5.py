# задача 3 необязательная.
# Даны два многочлена, которые вводит пользователь как две строки.
# Задача - сформировать многочлен, содержащий сумму многочленов, и вывести как строку.
#
# Степени многочленов могут быть разные.
#
# Например, на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re


# Не успела доделать к сроку сдачи 4 дз
from re import *


def parse_polynomial(polynomial):
    regex_multipliers = r'[+-] \d+|^\d+'
    regex_powers = r'(?<=\^)\d+'
    powers = list_to_int(findall(regex_powers, polynomial))
    multipliers = list_to_int(findall(regex_multipliers, polynomial))
    polynomial_d = dict()
    for i in range(len(powers)):
        polynomial_d[powers[i]] = multipliers[i]
    return polynomial_d


def list_to_int(num_list):
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i].replace(' ', ''))
    return num_list


def standardize_poly(poly):
    # add ^1 to the term in pow 1
    poly = poly.replace('x ', 'x^1 ')
    # add 1 as multiplier where necessary
    regex_multiplier_neg = r'- (?=x)'
    poly = sub(regex_multiplier_neg, '- 1', poly)
    regex_multiplier_pos = r'\+ (?=x)'
    poly = sub(regex_multiplier_pos, '+ 1', poly)
    # add x^0 to the free term
    regex_free_term = r' \d+(?= =)'
    poly = sub(regex_free_term, search(regex_free_term, poly).group() + 'x^0 ', poly)
    print(poly)
    return poly


def get_sum_polynomial(poly_1, poly_2):
    poly_1 = parse_polynomial(standardize_poly(poly_1))
    poly_2 = parse_polynomial(standardize_poly(poly_2))
    final_poly = ''
    final_poly_powers = list(poly_1.keys()) + list(poly_2.keys())
    final_poly_powers = set(final_poly_powers)
    for i in range(len(final_poly_powers) - 1, -1, -1):
        multiplier = poly_1.get(i, 0) + poly_2.get(i, 0)
        if multiplier == 1:
            poly_term = ' + ' + 'x^' + str(i)
        elif multiplier == -1:
            poly_term = ' - ' + 'x^' + str(i)
        elif multiplier == 0:
            poly_term = ''
        elif multiplier > 0:
            poly_term = ' + ' + str(multiplier) + 'x^' + str(i)
        else:
            poly_term = ' - ' + str(abs(multiplier)) + 'x^' + str(i)
        final_poly += poly_term
    regex_unnecessary = r'^ \+ |^ (?=-)|\^1|x\^0'
    final_poly = sub(regex_unnecessary, '', final_poly) + ' = 0'
    return final_poly


polynomial_1 = '2x^2 + 4x + 5 = 0'
polynomial_2 = '5x^3 - 3*x^2 - 12 = 0'

print(f"The sum of polynomials {polynomial_1} and {polynomial_2} is: {get_sum_polynomial(polynomial_1, polynomial_2)}")
