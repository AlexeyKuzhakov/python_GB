#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#Примеры:
#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

list_entered = input('Введите числа через пробел: ').split()
num_list = list(map(int, list_entered))
max_number = max(num_list)
print(f'{max_number} это максимальное число из списка: {num_list}')