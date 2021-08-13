import itertools

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen_tuple = (itertools.zip_longest(tutors, klasses, fillvalue='None')) # обрачиваем в генератор
# собираем поочередно первые элементы списков и получаем список кортежей
print(type(gen_tuple)) # <class 'itertools.zip_longest'> - работает как генератор, но класс вот такой...
print(next(gen_tuple)) # ('Иван', '9А')
print(next(gen_tuple)) # ('Анастасия', '7В')
print(next(gen_tuple)) # ('Петр', '9Б')
print(next(gen_tuple)) # ('Сергей', '9В')
print(next(gen_tuple)) # ('Дмитрий', '8Б')
print(next(gen_tuple)) # ('Борис', '10А')
print(next(gen_tuple)) # ('Елена', '10Б')
print(next(gen_tuple)) # ('None', '9А')
print(next(gen_tuple)) # StopIteration
