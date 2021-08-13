# Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [src[i+1] for i in range(len(src) - 1) if src[i] < src[i + 1]]

print(new_list) # [12, 44, 4, 10, 78, 123]


# Расширенный вариант решения
#new_list = []
#for i in range(len(src) - 1):
    #if src[i] < src[i+1]:
        #new_list.append(src[i+1])
