# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы AA часов в сутки,
# но пересыпать тоже вредно и не стоит спать более BB часов. Сейчас Аня спит HH часов в сутки.
# Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее
# AA часов, выведите “Недосып”, если же более BB часов, то выведите “Пересып”.
# Получаемое число AA всегда меньше либо равно BB.
# На вход программе в три строки подаются переменные в следующем порядке: AA, BB, HH.
# Обратите внимание на регистр символов: вывод должен в точности соответствовать описанному в задании,
# т. е. если программа должна вывести "Пересып"

a = int(input())
b = int(input())
h = int(input())
if a<=h<=b:
    print('Это нормально')
elif a>h<b:
    print('Недосып')
else:
    print('Пересып')