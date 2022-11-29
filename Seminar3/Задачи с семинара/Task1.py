# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

my_list = ['dfkxxxj5j4k', '4rfdfns012u', 'k930781-cvcxm', '54fcvbn-23u5']
symbol = input('Введите символ: ')

# РЕШЕНИЕ С ЦИКЛОМ В ЦИКЛЕ
# for item in my_list:
#     for char in item:
#         if char == symbol:
#             print(f'Символ {symbol} присутствует в строке {item}')
#             break
#     else:
#         print(f'Символ {symbol} не присутствует в строке {item}')


# РЕШЕНИЕ С IF ELSE
# for item in my_list:
#     if symbol in item:
#         print(f'Символ {symbol} присутствует в строке {item}')
#     else:
#         print(f'Символ {symbol} не присутствует в строке {item}')

# РЕШЕНИЕ СО СЧЕТЧИКОМ
for item in my_list:
    count = 0
    for i in range(len(item)):
        if symbol == item[i]:
            count +=1
            print(f'Символ {symbol} присутствует в строке {item} на {i} позиции')
    print(f'Символ {symbol} присутствует в строке {item} на {count} раз')