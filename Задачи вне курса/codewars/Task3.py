# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

s = input('Введите слова через пробел: ')

def find_short(s):
    l = min(map(len, s.split()))
    return l

print(f'Длина самого короткого слова равна: {find_short(s)}')