# Задача 20
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:

# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

# А русские буквы оцениваются так:

# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:

# Ввод:
# ноутбук
# Вывод:
# 12

user_word = input("Введите слово: ").upper()

# Списки букв для словарей
en_scrable = {}
en_dict_1_point = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
en_dict_2_point = ['D', 'G']
en_dict_3_point = ['B', 'C', 'M', 'P']
en_dict_4_point = ['F', 'H', 'V', 'W', 'Y']
en_dict_5_point = ['K']
en_dict_8_point = ['J', 'X']
en_dict_10_point = ['Q', 'Z']

ru_scrable = {}
ru_dict_1_point = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
ru_dict_2_point = ['Д', 'К', 'Л', 'М', 'П', 'У']
ru_dict_3_point = ['Б', 'Г', 'Ё', 'Ь', 'Я']
ru_dict_4_point = ['Й', 'Ы']
ru_dict_5_point = ['Ж', 'З', 'Х', 'Ц', 'Ч']
ru_dict_8_point = ['Ш', 'Э', 'Ю']
ru_dict_10_point = ['Ф', 'Щ', 'Ъ']

# Формируем английский словарь
for i in en_dict_1_point:
    en_scrable.setdefault(i, 1)
for i in en_dict_2_point:
    en_scrable.setdefault(i, 2)
for i in en_dict_3_point:
    en_scrable.setdefault(i, 3)
for i in en_dict_4_point:
    en_scrable.setdefault(i, 4)
for i in en_dict_5_point:
    en_scrable.setdefault(i, 5)
for i in en_dict_8_point:
    en_scrable.setdefault(i, 8)
for i in en_dict_10_point:
    en_scrable.setdefault(i, 10)

# Формируем русский словарь
for i in ru_dict_1_point:
    ru_scrable.setdefault(i, 1)
for i in ru_dict_2_point:
    ru_scrable.setdefault(i, 2)
for i in ru_dict_3_point:
    ru_scrable.setdefault(i, 3)
for i in ru_dict_4_point:
    ru_scrable.setdefault(i, 4)
for i in ru_dict_5_point:
    ru_scrable.setdefault(i, 5)
for i in ru_dict_8_point:
    ru_scrable.setdefault(i, 8)
for i in ru_dict_10_point:
    ru_scrable.setdefault(i, 10)

points = 0  # Сумма набранных очков за слово

# Проверяем какой словарь использовать английский или русский
if user_word[0] in en_scrable.keys():
    for letter in user_word:
        points += en_scrable.get(letter)
elif user_word[0] in ru_scrable.keys():
    for letter in user_word:
        points += ru_scrable.get(letter)

print(points)