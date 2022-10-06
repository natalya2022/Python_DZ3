# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functools import reduce

my_list = [2, 3, 5, 9, 3]
sum = 0
for i, val in enumerate(my_list):
    if (i % 2):
        sum += val
print(sum)

# 2 вариант решения

my_list = input('Введите целые числа разделённые пробелами ').split()
odd_sum = reduce(lambda sum, enum: sum + (int(enum[1]) if enum[0] % 2 else 0), enumerate(my_list), 0)
print(odd_sum)
