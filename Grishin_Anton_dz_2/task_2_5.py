# создать список, содержащий цены на товары
goods_prices = [57.8, 46.51, 97.1, 22.21, 432.57, 32.33, 74.43, 274.67, 21.55, 643.73, 345.21,
                65.73, 16.74, 104.84, 64.74]
new_goods_prices = []
# вывести на экран цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk>
# подумать, как из цены получить рубли и копейки
for price in goods_prices:
    r = int(price)  # отделяем рубли
    k = round((price - r) * 100)  # отделяем копейки
    new_goods_prices.append(f'{r} руб {k:02d} коп') # прописываем формат и добавляем в переменную
print(', '.join(new_goods_prices)) # чтобы не получать список, применяем join к строке
# выводим цены по возрастанию
print(id(goods_prices))
goods_prices.sort()
print(id(goods_prices)) # сверяем айди
print(goods_prices)
# создаем новый список, содержащий те же цены, но отсортированный по убыванию
alt_goods_prices = sorted(goods_prices, reverse=True)
print(alt_goods_prices)
# выводим цены самых дорогих пяти товаров
print(sorted(goods_prices[-5:]))
