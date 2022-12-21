# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

# x1 = float(input('Введите координату x1: '))
# y1 = float(input('Введите координату y1: '))
# x2 = float(input('Введите координату x2: '))
# y2 = float(input('Введите координату y2: '))
# distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
# print(round(distance, 2))

points_list = input('Введите координаты точек x1 y1 x2 y2 через пробел: ').split(' ')

while len(points_list) != 4:
    points_list = input('Координат должно быть четыре! Повторите ввод (через пробел): ').split(' ')

def distance(point_list):
    x1,y1,x2,y2 = list(map(float, point_list))
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

print(f'Расстояние между точками {round(distance(points_list),2)}')