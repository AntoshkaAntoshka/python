# Создаем переменные для финального вывода суммы
final_sum_1 = 0
final_sum_2 = 0
# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
list_of_num = [i**3 for i in range(1, 1000, 2)]
# Вычисляем сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
for i in list_of_num:
    x = i
    sum_number_1 = 0
    while i != 0:
        sum_number_1 += i % 10
        i = i // 10
    if sum_number_1 % 7 == 0:
        final_sum_1 += x
print(f'Итоговая сумма № 1  = {final_sum_1}')

# К каждому элементу списка добавим 17 и заново вычислим сумму чисел из списка, сумма цифр которых делится нацело на 7
for i in list_of_num:
    sum_number_2 = 0
    i += 17
    x = i
    while i != 0:
        sum_number_2 += i % 10
        i = i // 10
    if sum_number_2 % 7 == 0:
        final_sum_2 += x
print(f'Итоговая сумма № 2  = {final_sum_2}')