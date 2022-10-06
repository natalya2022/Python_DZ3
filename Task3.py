# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
print(my_list)
new_list = []
for index in range(len(my_list)):
    elem = my_list[index] - int(my_list[index])
    if elem > 0:        # Отбрасываем числа без дробной части
        new_list.append(round(elem, 3))
new_list.sort()
print(new_list, '=>', new_list[0] - new_list[-1])
