# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
import random
from random import randint

lens = int(input('Введите длину списка: '))
my_list = []
for i in range(lens):
    my_list.append(randint(10, 99))
print(my_list)

num = randint(0, len(my_list))
for i in range(len(my_list)):
    my_list[num], my_list[i-1] = my_list[i-1], my_list[num]
print(my_list)
