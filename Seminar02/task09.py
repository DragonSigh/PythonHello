# ЗАДАЧА №9

# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# Input: 5
# Output: 120

number_n = int(input("Введите целое неотрицательное число: "))
i = 1
result = 1

while i <= number_n:
    result *= i
    i += 1

print(result)