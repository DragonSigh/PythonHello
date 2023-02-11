# ЗАДАЧА №37

# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.

# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def reverse_seq(number):
    elem = input('Введите элемент: ')
    if number == 1:
        return elem
    return reverse_seq(number - 1) + ' ' + elem

print(reverse_seq(int(input('Введите количество элементов: '))))