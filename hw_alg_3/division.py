def division(div_dd, div_dr):
    if div_dr < 1:
        quit()
    result = 0
    while div_dd >= div_dr:
        div_dd -= div_dr
        result += 1
    return print(f'Частное: {result}, остаток: {div_dd}')

division(8,9)