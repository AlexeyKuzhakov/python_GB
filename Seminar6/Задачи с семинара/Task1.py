# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности:
#     Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# input_list = [1, 2, 3, 5, 1, 5, 3, 10]
#
# count = 0
# output_list = []
# for i in range(len(input_list)):
#     if input_list.count(input_list[i]) == 1:
#         output_list.append(input_list[i])
#
# print(output_list)


input_list = [1, 2, 3, 5, 1, 5, 3, 10, 10, 7]
my_dict = {}
my_set = set(input_list)
my_list_null = [0] * len(my_set)
my_dict2 = dict(zip(my_set, my_list_null))
output_list_2 = []

my_dict = set(input_list)
for i in input_list:
    my_dict2[i] += 1
for i in my_dict2.keys():
    if my_dict2.get(i) == 1:
        output_list_2.append(i)

print(output_list_2)