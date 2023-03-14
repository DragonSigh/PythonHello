# ЗАДАЧА №2 **

# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# (*) Усложнение. Решите для числа произвольной разрядности: произвольное количество цифр в числе.
# (**) Усложнение. Для числа произвольной разрядности добавить в вывод строку с числами, например так:

number = int(input('Введите число произвольной разрядности: '))
n = number
digit = 0
all_digits = ' + '.join(str(number))
result = 0

while n != 0:
    digit = n % 10
    result += digit
    n //= 10

print(f'Сумма чисел числа {number} равна {result} ({all_digits})')