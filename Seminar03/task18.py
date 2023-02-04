# ЗАДАЧА №18

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:

# 5
# 1 2 3 4 5
# 6
# -> 5

import random

number_n = int(input("Введите n - количество элементов в массиве: "))

# list_a = [i for i in range(1, number_n + 1)]  # массив как в условии
list_a = [random.randint(1, number_n) for i in range(1, number_n + 1)]  # массив случайных чисел

print(list_a)

number_x = int(input("Введите x - какое число нужно найти: "))

result = 0

if number_x <= min(list_a):
    result = min(list_a)
elif number_x >= max(list_a):
    result = max(list_a)
else:
    for i in range(1, len(list_a)):
        if abs(list_a[i] - number_x) < abs(result - number_x):
            result = list_a[i]

print(result)