# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.

# Ввод:
# 1 2 3 2 3 

# Вывод:
# 2

import random

rand_list_size = int(input('Ведите размер массива: '))
rand_list = [random.randint(1, 10) for i in range(0, rand_list_size)]

unique_elems = set(rand_list)

counter = 0

for elem in unique_elems:
    if rand_list.count(elem) % 2 == 0:
        counter += rand_list.count(elem) // 2

print(rand_list)
print(counter)