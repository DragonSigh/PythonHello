# ЗАДАЧА №35

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes

def is_prime(number):
    if number % 2 == 0:
        return number == 2
    # Перебор нечетных делителей, если число не делится на 2
    d = 3
    while d * d <= number and number % d != 0:
        d += 2
    return d * d > number

check_number = int(input())
print(is_prime(check_number))