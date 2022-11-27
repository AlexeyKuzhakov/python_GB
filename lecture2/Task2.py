def concatenatio(*params):
    res: str = ''
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'q', 'w'))
print(concatenatio('a', '1'))