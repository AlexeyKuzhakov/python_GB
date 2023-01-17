from bot_config import dp, bot
from aiogram import types
from random import randint


candies = 150

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    global candies
    await bot.send_message(message.from_user.id, text=f'{message.from_user.first_name},'
                                                      f' давай сыграем в игру? '
                                                      f'На столе лежит {candies} конфет, мы будем брать по '
                                                      f'очереди конфеты и кто заберет последние тот и победил')


@dp.message_handler()
async def anything(message: types.Message):
    global candies
    if message.text.isdigit():
        candies -= int(message.text)
        if 0 < int(message.text) < 29:
            await bot.send_message(message.from_user.id, f'{message.from_user.first_name},'
                                                         f' взял со стола {message.text} конфет. '
                                                         f'На столе осталось {candies}')
            if candies < 29:
                await bot.send_message(f'{message.from_user.first_name} на столе осталось {candies} конфет, '
                                    f'заберу пожалуй все. ')
                await bot.send_message(f'Спасибо за игру, я победил!'
                                    f' Но ты не расстраивайся, мы можем сыграть еще раз. ')
            else:
                k = randint(1, 28)
                candies -= k
                await bot.send_message(message.from_user.id, f'{message.from_user.first_name},'
                                                             f' я взял {k} конфет. '
                                                             f'На столе осталось {candies} ')
                if candies < 29:
                    await bot.send_message(f'{message.from_user.first_name} на столе осталось {candies} конфет, '
                                           f'можашь забрать все. А я смирюсь с поражением! ')
                else:
                    await bot.send_message(f'{message.from_user.first_name} теперь твой ход, сколько возмешь?')
        else:
            await message.reply(f'{message.from_user.first_name} забыл предупредить, можно брать не больше 28, '
                                f'возьми поменьше')
