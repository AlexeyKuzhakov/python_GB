# my_list = []
#
# while True:
#     string = input('Введите число и нажмите ентер: ')
#     for i in string:
#         if not i.isdigit():
#             break
#     else:
#         if string != '':
#             my_list.append(int(string))
#         else:
#             break
#
# print(my_list)

# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел

def concatinatio(*params):
    res: str = ''
    for item in params:
        res += item
    return res

def MaxInlist(list):
    max = list[0]
    for i in range(1, len(list)):
        if max < list[i]:
            max = list[i]
    return max

def MinInlist(list):
    min = list[0]
    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
    return min

my_list = input('Введите числа через пробел: ')
my_list = my_list.strip().split(' ')

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

print(f'Максимальное число: {MaxInlist(my_list)}\nМинимальное число: {MinInlist(my_list)}')