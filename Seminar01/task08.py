# ЗАДАЧА №8

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

num_n = int(input('Введите число N: '))
num_m = int(input('Введите число M: '))

x = num_n

if num_n > num_m:
    x = num_m

num_k = int(input('Введите сколько долек отломить: '))

print(num_n, num_m, num_k, '->', 'yes' if num_k % x == 0 else 'no')