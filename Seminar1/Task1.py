# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#*Примеры:*
#- 5, 25 -> да
# 4, 16 -> да
#- 25, 5 -> да
#- 8,9 -> нет

print('Введите первое число')
a = int(input())
print('Введите второе число')
b = int(input())
if a == b*b:
    print(f'{a} является квадратом {b}')
elif b == a*a:
    print(f'{b} является квадратом {a}')
else:
    print('Введенные числа не являются квадратом')
