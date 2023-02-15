# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint

min_number = int(input('Введите минимальное число: ')) # 7
max_number = int(input('Введите максимальное число: ')) # 10
# input_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
input_list = [randint(1, 100) for i in range(randint(5, 10), randint(15, 20))]
result = []

print(input_list)

for i in range(0, len(input_list)):
    if min_number <= input_list[i] <= max_number:
        result.append(i)

print(result)