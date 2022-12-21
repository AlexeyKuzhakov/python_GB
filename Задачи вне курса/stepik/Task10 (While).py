# Треугольник из звездочек

# n = int(input('Число строк: '))
# c = 1
# while c <=n:
#     print('*' * c)
#     c += 1

# n = int(input('Число строк: '))
# stars = '*'
# while len(stars) <= n:
#     print(stars)
#     stars += '*'

# Сколько всего знаков * будет выведено после исполнения фрагмента программы:
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1

# Посчитать сумму чисел от a до b
a = int(input())
b = int(input())
s = 0
i = a
while i <= b:
    s += i
    i += 1
print(s)