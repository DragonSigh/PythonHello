# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам

# Вывод:
# Парам пам-пам

# input_phrase = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
input_phrase = input()

def check_rhyme(phrase, vowels_info = True):
    vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
    phrase_list = phrase.split(' ')
    result_vowels = []
    result = []

    for elem in phrase_list:
        phrase_vowels = dict()
        counter = 0
        for s in elem:
            if s in vowels:
                counter += 1
                phrase_vowels[s] = phrase_vowels.get(s, 0) + 1
        result_vowels.append(phrase_vowels)
        result.append(counter)

    if vowels_info:
        return result.count(result[0]) == len(result), result_vowels
    else:
        return result.count(result[0]) == len(result)

print(check_rhyme(input_phrase))