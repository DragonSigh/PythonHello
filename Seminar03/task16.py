# ЗАДАЧА №16

# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai . Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

import random

number_n = int(input("Введите n - количество элементов в массиве: "))

# list_a = [i for i in range(1, number_n + 1)]  # массив как в условии
list_a = [random.randint(1, number_n) for i in range(1, number_n + 1)]  # массив случайных чисел

print(list_a)

number_x = int(input("Введите x - какое число нужно найти: "))

result = list_a.count(number_x)

print("-1" if result == 0 else result)