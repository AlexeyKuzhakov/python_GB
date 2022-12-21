# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

# my_list = list(map(int,input('Введите числа через пробел: ').split()))
# print(f'Введенный список: {my_list}')
#
# res_list = []
# while len(my_list) > 1:
#     res_list.append(my_list[0] * my_list[-1])
#     del my_list[0]
#     del my_list[-1]
# if len(my_list) == 1:
#     res_list.append(my_list[0]**2)
# print(f'Итоговый список: {res_list}')

def mult_list(list):
    length = len(list) // 2 + 1 if len(list) % 2 != 0 else len(list) // 2
    new_list = [list[i] * list[len(list) - i - 1] for i in range(length)]
    print(f'Итоговый список: {new_list}')

list = list(map(int, input("Введите числа через пробел: ").split()))
mult_list(list)