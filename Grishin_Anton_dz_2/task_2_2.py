phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_phrase = []
for el in phrase:
    if el.isdigit(): # находим целые числа в списке
        num = int(el)
        new_phrase.extend(['"', f'{num:02d}', '"'])
    elif el.startswith('+'): # находим плюс)))
        num = int(el)
        new_phrase.extend(['"', f'+{num:02d}', '"'])
    else:
        new_phrase.append(el)
print(new_phrase)
final_phrase = ''.join(new_phrase) # склеиваем в строку, разделяя пробелами.
print(final_phrase) # в ответе остались пробелы. не понял, как их убрать
