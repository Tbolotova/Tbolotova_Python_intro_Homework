# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random


def set_coin_states(total_coin_count):
    coin_states = []
    for i in range(total_coin_count):
        current_coin_state = random.choice(["heads", "tails"])
        coin_states.append(current_coin_state)
    print(f"The coins are facing the following sides up: {coin_states}")
    return coin_states


def find_min_coin_num(coins_state):
    heads_count = 0
    tails_count = 0
    for el in coins_state:
        if el == "heads":
            heads_count += 1
        if el == "tails":
            tails_count += 1
    if heads_count > tails_count:
        return tails_count
    else:
        return heads_count


coin_num = random.randrange(1, 50)
min_coin_num_to_flip = find_min_coin_num(set_coin_states(coin_num))
print(f"We need to flip at least {min_coin_num_to_flip} coins to make all of them face the same side up")