print('Введите число A')
a = int(input())
print('Введите число B')
b = int(input())
print(a, '+', b, '=', a+b)
print(a, '*', b, '=', a*b)
c = round(a/b)
print(f'{a} / {b} = {c}')

list = [1, 3, 4]
print('Список', list)

if a in list:
    print(f'Число {a} есть в списке')
else:
    print(f'Числа {a} нет в списке')