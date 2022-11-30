# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

lens = int(input('Введите длину списка: '))
my_list = []

for i in range(lens):
    my_list.append(round(uniform(1, 99), 2))
print(f'Рандомный список: {my_list}')

res_list = []
for i in range(lens):
    res_list.append(round(my_list[i] - int(my_list[i]), 2))

print(f'Разница между max и min дробной части списка: {round(max(res_list) - min(res_list), 2)}')