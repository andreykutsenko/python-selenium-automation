# TODO: Домашнее задание: Написать программу для числа из любого количества цифр.
#  Вместо числа из 3 цифр, нужно считать сумму числа из n цифр.
#  Где  n вводит пользователь с клавиатуры. Только положительные.

from random import randint

n = int(input('Введите количество цифр > 0: '))

def start_end_random(n):
    start = '1'
    end = '9'
    i = 1
    if n > 1:
        while i <= (n - 1):
            start += '0'
            end += '9'
            i += 1
    return randint(int(start),int(end))

if n > 0:
    m = start_end_random(n)
    print(f'Мы получили случайное {n}-значное число: {m}')
    l = list(str(m))
    sum = 0
    # print(l[0])
    for item in l:
        sum += int(item)
    print(f'Сумма чисел = {sum}')
else:
    print('Количество цифр д.б. > 0')
