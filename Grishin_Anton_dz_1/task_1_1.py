# запрашиваем у пользователя число
duration = int(input('Введите время в секундах: '))
# вводим переменные: часы, минуты, секунды
d = duration // 86400
h = duration // 3600
m = (duration - h * 3600) // 60
s = duration - (h * 3600 + m * 60)
# проводим ветвление
if duration < 60:
    print(s, 'сек')
elif 60 < duration <= 3600:
    print(m, 'мин', s, 'сек')
elif 3600 < duration <= 86400:
    print(h, 'час', m, 'мин', s, 'сек')
else:
    if 86400 < duration <= 604800:
        print(d, 'дней', h, 'час', m, 'мин', s, 'сек')