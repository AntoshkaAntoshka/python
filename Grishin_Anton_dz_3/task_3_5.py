import random

def get_jokes(count, flag =False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(count): # запускаем каждую шутку в цикл
        noun = random.choice(nouns)
        adverb = random.choice(adverbs)
        adjective = random.choice(adjectives)
        joke = (f'{noun} {adverb} {adjective}') # рандомим три слова и формируем шутку
        not_repeat_jokes = [] # хочу, чтобы переменная принимала результат значения от 15 строки, но она все равно серая
        print(joke)
        if flag == True:
            not_repeat_jokes = joke.split() # разделяем шутку и передаем список (но он не передается почему-то)
            for noun in nouns:
                for i in not_repeat_jokes:
                    if noun == i:
                        nouns.remove(noun)
            for adverb in adverbs:
                for i in not_repeat_jokes:
                    if i == adverb:
                        adverbs.remove(adverb)
            for adjective in adjectives:
                for i in not_repeat_jokes:
                    if i == adjective:
                        adjectives.remove(adjective)


print(get_jokes(3, flag=False))

# код работает, но часть с заданием со звездочкой не хочет считывать

