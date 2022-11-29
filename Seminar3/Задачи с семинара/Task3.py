# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять
# количество вхождений одной строки в другой.

text = 'Первое число - 1, второе число - 2, сумма 3'
sub_text = input('Введите подстроку: ')
count = 0
# print(text.count(sub_text))

for i in range(len(text)):
    if text[i:i:len(sub_text)] == sub_text:
        count += 1
print(f'Подстрока {sub_text} встречается в тексте {count} раз')