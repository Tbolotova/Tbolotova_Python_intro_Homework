# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
# Теперь надо проверить ее практически
# в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением
# и засекаем общее время выполнения программы
# юзаем библиотеки random и time
# предикаты НЕ ЗАДАЕМ как целое число!

import random
import time


def check_logical_expression(predicates, result_list):
    left = not all(predicates)
    right = [not el for el in predicates]
    is_correct = not all(predicates) == [not el for el in predicates]
    result_list.append(is_correct)
    print(f"Expression for {predicates} is {is_correct}")


def generate_predicates():
    predicate_num = random.randint(3, 15)
    predicate_list = []
    for k in range(1, predicate_num):
        predicate_list.append(random.choice([True, False]))
    return predicate_list


start_time = time.time()
check_list = []
for i in range(100):
    check_logical_expression(generate_predicates(), check_list)
print(f"The result of the 100 checks for all predicates is: {all(check_list)}")
print(f"Total time of execution is {time.time() - start_time}")
