# ЗАДАЧА №17

# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Примечание: Пользователь может вводить значения списка или список задан изначально.

numbers_list = [1, 1, 2, 0, -1, 3, 4, 4]
count = 1
numbers_list.sort()

for i in range(0, len(numbers_list) - 1):
    if numbers_list[i] != numbers_list[i + 1]: count += 1

print(count)