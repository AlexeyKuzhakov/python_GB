print('Введите число A')
a = int(input())
print('Введите число B')
b = int(input())
print(a, '+', b, '=', a+b)
print(a, '*', b, '=', a*b)
c = round(a/b)
print(f'{a} / {b} = {c}')

list = [1, 3, 4]

if a in list:
    print(f'Число {a} есть в списке')
else:
    print(f'Числа {a} нет в списке')

print('Введите ваше имя')
name = input()
if name == 'Алексей':
    print('Добрый день', name)
elif name == 'Леша':
    print('Привет', name)
else:
    print(name, ', вас не ждали')

#инверсия числа
print('Введите целое число: ')
original = int(input())
if original % 2 ==0:
    inverted = 0
    while original != 0:
        inverted = inverted * 10 + (original % 10)
        original //= 10
    print(inverted)
else:
    print('Вы ввели не целое число')

print('Квадраты чисел из списка: ', list)
for i in list:
    print(i**2)

print(f'Список от нуля до введенного вами первого числа "{a}": ')
for j in range(a):
    print(j)