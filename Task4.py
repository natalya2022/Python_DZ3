# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

decnum = int(input('Введите десятичное число '))
binnum = ''
while decnum > 0:
    binnum = str(decnum % 2) + binnum
    decnum = decnum // 2
print(binnum)