# ЗАДАЧА №12

# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

summa  = int(input("Введите сумму загаданных чисел: "))
product = int(input("Введите произведение загаданных чисел: "))

for number_x in range (1, 1000):
    number_y = summa - number_x
    if number_x <= number_y and number_x * number_y == product:
        print(summa, product, '->', number_x, number_y)
        break