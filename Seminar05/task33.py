# ЗАДАЧА №33

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

def change_grades(grades_list):
    max_grade = max(grades_list)
    min_grade = min(grades_list)
    for i in range(0, len(grades_list)):
        if grades_list[i] == max_grade:
            grades_list[i] = min_grade
    return grades_list

grades = int(input('Введите количество оценок: '))
journal = [randint(1, 5) for i in range(1, grades + 1)]

print(journal)
print(change_grades(journal))