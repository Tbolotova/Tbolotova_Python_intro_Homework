# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты
# высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего
# модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.
from random import *


def get_max_harvest_bush(bush_harvest):
    harvest_reps = []
    for i in range(len(bush_harvest)):
        if i + 1 == len(bush_harvest):
            harvest_reps.append(bush_harvest[i - 1] + bush_harvest[i] + bush_harvest[0])
        else:
            harvest_reps.append(bush_harvest[i - 1] + bush_harvest[i] + bush_harvest[i + 1])
    max_harvest = max(harvest_reps)
    return max_harvest


def populate_bushes(bush_num):
    harvest_per_bush = []
    for i in range(bush_num):
        # числа от 1 до 10 поставила для простоты проверки результата
        harvest_per_bush.append(randint(1, 10))
    return harvest_per_bush


bush_number = 15
bushes_harvest = populate_bushes(bush_number)
print(f"Max harvest per rep in the patch of {bushes_harvest} is {get_max_harvest_bush(bushes_harvest)}")
