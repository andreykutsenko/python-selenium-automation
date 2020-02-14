# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input('Введите число > 0: '))
if n > 0:
    l = list(str(n))
    L_even = []
    L_odd = []
    even = 0
    odd = 0
    print(f'В вашем числе = {n}:')
    for item in l:
        if int(item) % 2 == 0:
            even += 1
            L_even.append(int(item))
        else:
            odd += 1
            L_odd.append(int(item))
    if even == 0:
        print(f'нет четных чисел')
    else:
        print(f'{even} четн. чис. {L_even}')
    if odd == 0:
        print(f'и нет нечетных чисел')
    else:
        print(f'и {odd} нечетн. чис. {L_odd}')
else:
    print('Число д.б. > 0')