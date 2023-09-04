"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `list_1` и `k`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `list_1` и `k` для проверки
"""
from math import *

list_1 = [1, 2, 3, 4, 5]
k = 6

# Введите ваше решение ниже
min_diff = abs(list_1[0] - k)
closest_el = list_1[0]

for i in list_1:
    current_diff = abs(i - k)
    if current_diff < min_diff:
        min_diff = current_diff
        closest_el = i

print(closest_el)