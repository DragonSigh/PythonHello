num = int(input())
digit4 = (num % 10 ** 1) // 10 ** 0
digit3 = (num % 10 ** 2) // 10 ** 1
digit2 = (num % 10 ** 3) // 10 ** 2
digit1 = (num % 10 ** 4) // 10 ** 3

print(digit1, digit2, digit3)

print(f'Цифра в позиции тысяч равна {digit1}')
print(f'Цифра в позиции сотен равна {digit2}')
print(f'Цифра в позиции десятков равна {digit3}')
print(f'Цифра в позиции единиц равна {digit4}')