# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""

from random import randint

def input_dat(name):
    x = int(input(f"{name}, возьмите конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, можно взять не более 28 конфет: "))
    return x

def p_print(name, k, counter, value):
    print("=" * 58)
    print(f"{name} взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите ваше имя: ")
player2 = "Умный бот"
candies = int(input("Введите количество конфет на столе: "))
turn = randint(0, 2)
if turn:
    print("=" * 44)
    print(f"Бросаем жребий...Первый ходит {player1}.")
else:
    print("=" * 44)
    print(f"Бросаем жребий...Первый ходит {player2}.")

counter1 = 0
counter2 = 0

while candies > 28:
    if turn:
        k = input_dat(player1)
        counter1 += k
        candies -= k
        turn = False
        p_print(player1, k, counter1, candies)
    else:
        k = randint(1, 28)
        counter2 += k
        candies -= k
        turn = True
        p_print(player2, k, counter2, candies)

if turn:
    print("=" * 58)
    print(f"{player1}, поздравляю, ты выиграл!")
else:
    print("=" * 58)
    print(f"{player2} тебя обыграл, не расстраивайся, попробуй сыграть еще раз!")