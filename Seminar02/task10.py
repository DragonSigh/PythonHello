# ЗАДАЧА №10

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

import random

number_of_coins = int(input("Введите количество монеток: "))
coins_list = list()

one_side_count = 0
second_side_count = 0

for i in range(0, number_of_coins):
    coins_list.append(random.randint(0, 1))
    if coins_list[i] == 0:
        one_side_count += 1
    else:
        second_side_count += 1

print(number_of_coins, "->", coins_list)
print(one_side_count if one_side_count <= second_side_count else second_side_count)