# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# возводит число А в целую степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def num_power(number, power):
    if power == 0:
        return 1
    power -= 1
    return num_power(number, power) * number

num_a = int(input('Введите число: '))
num_b = int(input('Введите степень: '))

print(num_power(num_a, num_b))