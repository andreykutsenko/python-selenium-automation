# Найти максимальное число из трех. Вводятся три целых числа. Определить какое из них наибольшее.

L = []
i = 0
while i < 3:
    L.append(int(input(f'Введите {i + 1}-е число: ')))
    i += 1
print(f'В массиве чисел {L} максимальное = {max(L)}')


# n1 = int(input('Введите первое число: '))
# max_n = n1
# n2 = int(input('Введите второе число: '))
# if max_n < n2:
#     max_n = n2
# n3 = int(input('Введите третье число: '))
# if max_n < n3:
#     max_n = n3
# print(f'Максимальное число: {max_n} \nиз 3-х чисел: {n1}, {n2}, {n3}')