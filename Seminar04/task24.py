# ЗАДАЧА №24

# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.

# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9
import random
bushes = int(input('Ведите количество кустов: '))
berries = [random.randint(1, 10) for i in range(1, bushes + 1)]
max_sum = 0
max_bush = 0

for i in range(0, bushes):
    if i == bushes - 1:
        current_sum = berries[i - 1] + berries[i] + berries[0]
    else:
        current_sum = berries[i - 1] + berries[i] + berries[i + 1]
    if current_sum > max_sum:
        max_sum = current_sum
        max_bush = i

print(bushes, '->', *berries)
print(f'Макс. кол-во ягод {max_sum}, собрано для куста {max_bush}')