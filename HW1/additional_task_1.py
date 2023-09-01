# Посчитать сумму цифр любого целого или вещественного числа, число вводит пользователь. Через строку решать нельзя.

from fractions import Fraction
from decimal import Decimal

number = Fraction(Decimal(input("Please enter a number: ")))

while number % 10 != 0:
    number *= 10

sum_digits = 0
while number >= 1:
    sum_digits += number % 10
    number = number // 10

print(sum_digits)
