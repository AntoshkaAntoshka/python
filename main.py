# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
numbers = []
def max_number():
    for i in range(3):
        number = int(input('Введите число: '))
        numbers.append(number)
    return max(numbers)
print(max_number())