# ЗАДАЧА №15

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

number_of_watermelons = int(input("Введите количество арбузов у продавца: "))
weights_list = list()

i = 0

for i in range(0, number_of_watermelons):
    weights_list.append(random.randint(1,10))

max_weight = weights_list[0]
min_weight = weights_list[0]

for i in range(0, number_of_watermelons):
    if weights_list[i] > max_weight:
        max_weight = weights_list[i]
    if weights_list[i] < min_weight:
        min_weight = weights_list[i]

print(number_of_watermelons, "->", weights_list)
print(min_weight, max_weight)