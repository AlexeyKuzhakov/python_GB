# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +, -, /, *
# Приоритет операций стандартный

string = '1 + 2 * 3'
print(string)
list = string.split()
print(list)
for i in range(len(list)):
    if list[i].isdigit():
        list[i] = int(list[i])
print(list)

result = 0

while len(list) != 1:
    i = 0
    while ('*' in list or '/' in list) and i < len(list):
        if list[i] == '*':
            result = list[i-1] * list[i+1]
            list.pop(i)
            list.pop(i)
            list[i-1] = result
        elif list[i] == '/':
            result = list[i-1] / list[i+1]
            list.pop(i)
            list.pop(i)
            list[i-1] = result
        else:
            i += 1
    while ('+' in list or '-' in list) and i < len(list):
        if list[i] == '+':
            result = list[i - 1] + list[i + 1]
            list.pop(i)
            list.pop(i)
            list[i - 1] = result
        elif list[i] == '-':
            result = list[i - 1] - list[i + 1]
            list.pop(i)
            list.pop(i)
            list[i - 1] = result
        else:
            i += 1

print(list)