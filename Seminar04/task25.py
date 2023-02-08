# ЗАДАЧА №25

# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()

chars_line = 'a a a b c a a d c d d'
chars_list = chars_line.split()
chars_counter = {}
result = ''

for i in chars_list:
    chars_counter.setdefault(i, 0)

for elem in chars_list:
    if chars_counter[elem] > 0:
        result += f'{elem}_{chars_counter[elem]} '
    else:
        result += f'{elem} '
    chars_counter[elem] += 1
    
print(result)