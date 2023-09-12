# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# Функция не должна ничего выводить, только возвращать значение.
#
# Пример:
#
#
# sum(2, 2)
# # 4

def sum(a, b):

    if b == 0:
        return a
    if b < 0:
        return sum(a, b + 1) - 1
    else:
        return sum(a, b - 1) + 1


print(sum(3, 4))

# def sum(x, y):
#     if (y == 0):
#         return x;
#     else:
#         return (1 + sum(x, y - 1));
#
#
# x = int(input("Enter number first number: "))
# y = int(input("Enter number second number: "))
#
# print("Sum of two numbers are: ", sum(x, y))