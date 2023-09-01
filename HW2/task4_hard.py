# Задача 1 HARD по желанию
# Напишите программу, которая принимает на вход целое или дробное число и выдаёт
# количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4

from decimal import Decimal

def get_digit_number(num):
    num_integer = int(num)
    num_decimal = num % 1
    digits_integer = 0
    digits_decimal = 0

    if num_integer == 0:
        digits_integer = 1
    else:
        while num_integer >= 1:
            digits_integer += 1
            num_integer /= 10

    while num_decimal % 1 != 0:
        num_decimal *= 10
        digits_decimal += 1

    return digits_integer + digits_decimal


number = input("Please enter a number: ")
print(f"The number of digits in the number {number} is {get_digit_number(Decimal(number))}")
