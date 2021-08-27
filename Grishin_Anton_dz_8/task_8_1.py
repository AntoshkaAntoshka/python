# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря.Если адрес не валиден,выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
import re

def email_parse(e_mail):
    pattern = re.compile(r'(?P<username>[A-z0-9/.]+)@(?P<domain>\w+\.\w+)')
    result = pattern.match(e_mail)

    if result:
        return result.groupdict()

    raise ValueError(f'Incorrect e-mail: {e_mail}')

print(email_parse('antongri.shin1994@mail.ru'))