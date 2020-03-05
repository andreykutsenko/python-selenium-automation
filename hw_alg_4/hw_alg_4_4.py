number = int(input(f'Введите число: '))
exponent = int(input(f'Введите степень числа: '))

def exponentiation(number, exponent):
    number = abs(number)
    exponent = abs(exponent)
    if exponent == 0:
        return 1
    else:
        return number * exponentiation(number, exponent-1)

print(exponentiation(number, exponent))