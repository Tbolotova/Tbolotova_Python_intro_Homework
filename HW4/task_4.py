# задача 2 необязательная. Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции
def convert_to_notation(num: int, notation: int) -> str:
    check_bin = bin(num)
    check_oct = oct(num)
    result = ''
    while num >= 1:
        result = str(num % notation) + result
        num = num // notation

    # checks
    # if notation == 2:
    #     print('0b' + result == check_bin)
    # elif notation == 8:
    #     print('0o' + result == check_oct)

    return result


number = int(input("Please enter a number: "))
print(f'Binary representation of {number} is {convert_to_notation(number, 2)}')
print(f'Octal representation of {number} is {convert_to_notation(number, 8)}')