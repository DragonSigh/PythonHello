# ЗАДАЧА №11

# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6

number_a = int(input("Введите натуральное число > 1: "))
fibo1 = 0
fibo2 = 1
counter = 2

if number_a <= 1:
    print("Error")
else:
    while True:
        fibo1 += fibo2
        counter += 1

        if fibo1 == number_a:
            print(counter)
            break

        fibo2 += fibo1
        counter += 1

        if fibo2 == number_a:
            print(counter)
            break

        if fibo2 > number_a:
            print("-1")
            break