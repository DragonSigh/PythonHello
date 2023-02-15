# Задача №45

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 10**5 . Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод:
# 300

# Вывод:
# 220 284

def find_sum_of_dividers(number):
    sum_of_dividers = 0

    for i in range(number - 1, 1, -1):
        if (number % i == 0):
            sum_of_dividers += i
    return sum_of_dividers + 1


number_k = int(input())

while number_k >= 10 ** 5:
    print(f'Ошибка ввода, введите число меньше {10 ** 5}')
    number_k = int(input())

# temp_sum = find_sum_of_dividers(220)
# temp_2_sum = find_sum_of_dividers(temp_sum)

# print(temp_sum, temp_2_sum)

for i in range(1, number_k):
     temp_sum = find_sum_of_dividers(i)
     temp_2_sum = find_sum_of_dividers(temp_sum)

     if i < temp_sum <= number_k and i == temp_2_sum:
         print(temp_2_sum, temp_sum)