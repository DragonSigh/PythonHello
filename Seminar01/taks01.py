# ЗАДАЧА №1

# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# Input:
# n = 700
# m = 750
# Output:
# 2

num_n = int(input('Введите число n: '))
num_m = int(input('Введите число m: '))

result = (num_m + num_n - 1) // num_n

print(result)