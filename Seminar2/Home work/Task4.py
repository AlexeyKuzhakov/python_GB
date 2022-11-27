# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

from random import randint

lens = int(input('Введите длину списка: '))
my_list = []
for i in range(lens):
    my_list.append(randint(1000, 9999))
print(f'1 этап: {my_list}')

num_del = input('Введите цифру для удаления из списка: ')
my_str = ''
for i in my_list:
    my_str += str(i)+ ' '
del_str = my_str.replace(num_del, '')
del_list = list(map(int, del_str.split()))
print(f'2 этап: {del_list}')

res_str = list(map(str, del_list))
new_str = []
for number in res_str:
    while len(number)>1:
        summ = 0
        for digit in number:
            summ += int(digit)
            number = str(summ)
    else:
        new_str.append(number)
new_list = list(map(int, new_str))
print(f'3 Этап: {new_list}')

result = list(set(new_list))
print(f'4 Этап: {result}')
