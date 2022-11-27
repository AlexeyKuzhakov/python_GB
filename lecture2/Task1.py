# Добавление данных в файл
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# # data.writelines(colors)
# data.write('Line12\n')
# data.write('Line13\n')
# data.close()

# Второй способ добавления данных в файл
# with open('file.txt', 'a') as data:
#     data.write('Line7\n')
#     data.write('Line8\n')

# Чтение файла
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()