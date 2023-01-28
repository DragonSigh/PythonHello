# ЗАДАЧА 2

# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трёхзначное число: "))
n = number
digit = 0
result = 0

while n != 0:
    digit = n % 10
    result = result + digit
    n = n // 10

print(number, "->", result)