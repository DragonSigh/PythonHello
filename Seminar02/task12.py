# ЗАДАЧА №12

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

import math

summa  = int(input("Введите сумму загаданных чисел: "))
product = int(input("Введите произведение загаданных чисел: "))

# СПОСОБ №1: РЕШЕНИЕ ПЕРЕБОРОМ

# for number_x in range (1, 1000):
#     number_y = summa - number_x
#     if number_x <= number_y and number_x * number_y == product:
#         print(summa, product, '->', number_x, number_y)
#         break

# СПОСОБ №2: РЕШЕНИЕ КВАДРАТНЫМ УРАВНЕНИЕМ

# x + y = S
# x * y = P

# (S - y) * y = P
# y ** 2 - y * S + P = 0

a = 1
b = -summa
c = product

discriminant = b * b - 4 * a * c

# если дискриминант отрицательный - действительных корней нет;
if discriminant < 0:
    print(summa, product, '->', 'Решения нет')
# если дискриминант равен нулю, вычислить единственный корень уравнения по формуле х = −b/2a;
elif discriminant == 0:
    number_y = int(-b / 2 * a)
    number_x = summa - number_y
    print(summa, product, '->', number_x, number_y)
# если дискриминант положительный, найти два действительных корня квадратного уравнения по формуле корней 
else:
    number_y = int((-b + math.sqrt(discriminant)) / (2 * a))
    number_x = summa - number_y
    print(summa, product, '->', number_x, number_y)
