# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# 6 12

n_size = int(input('Введите n -  кол-во элементов первого множества: '))
m_size = int(input('Введите m -  кол-во элементов второго множества: '))

n_set = {int(input(f'Введите элемент {i + 1} множества n: ')) for i in range(0, n_size)}
m_set = {int(input(f'Введите элемент {i + 1} множества m: ')) for i in range(0, m_size)}

result = sorted(n_set.intersection(m_set))

if len(result) > 0:
    print(*result)
else:
    print('Повторяющихся чисел нет')