# Допущение: первое число в ряду Фибоначчи = 0, порядковый номер первого числа = 1

def fibonacci_list(n_x, n):
    # n_x - порядковый номер числа в ряду (начинается с 1)
    # n - количество чисел в ряду
    fibonacci_1 = 1
    fibonacci_2 = 1
    l_fibonacci = []
    if n == 1:
        l_fibonacci = [0]
    if n > 1:
        l_fibonacci = [0, fibonacci_1]
    if n > 2:
        l_fibonacci.append(fibonacci_2)
    i = 0
    while i < n - 3:
        fibonacci_sum = fibonacci_1 + fibonacci_2
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_sum
        i +=1
        l_fibonacci.append(fibonacci_sum)
    if n_x < n + 1 and n_x > 0:
        print(l_fibonacci[n_x-1])
        print(l_fibonacci)
    elif n < 1:
        print(f'Числовой ряд не сформирован')
    else:
        print(f'Не обнаружена числа в ряду с порядковым № {n_x}')

def fibonacci(n_x):
    fibonacci_1 = 1
    fibonacci_2 = 1
    if n_x == 1:
        print(0)
    if n_x == 2:
        print(fibonacci_1)
    if n_x == 3:
        print(fibonacci_2)
    i = 0
    while i < n_x - 3:
        fibonacci_sum = fibonacci_1 + fibonacci_2
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_sum
        i += 1
        if n_x == i + 3:
            print(fibonacci_sum)

# fibonacci_list(4,4)

fibonacci(8)
