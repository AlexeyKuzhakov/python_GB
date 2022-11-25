# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.

n = int(input('Введите число: '))
my_list = [round((1+1/n)**n, 2) for n in range(1, n+1)]
summ = round(sum(my_list), 2)
print(*my_list, sep= ', ')
print(f'Сумма чисел {summ}')
