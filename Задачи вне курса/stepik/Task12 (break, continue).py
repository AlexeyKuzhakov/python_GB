# Перемножаем два числа, пока не будут введены 0 0
# i = 0
# while i < 5:
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     if (a == 0) and (b == 0):
#         break # досрочно завершаем цикл
#     print(a * b)
#     i += 1

# i = 0
# while i < 5:
#     a, b = input().split()
#     a = int(a)
#     b = int(b)
#     if (a == 0) and (b == 0):
#         break # досрочно завершаем цикл
#     if (a == 0) or (b == 0):
#         continue # переходим к следующей итерации
#     print(a * b)
#     i += 1

# Определите, какое значение будет иметь переменная i после выполнения следующего фрагмента программы:

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
# print(i)

i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(i)