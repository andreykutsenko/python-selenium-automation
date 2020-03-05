string = input(f'Введите строку ')
n = input(f'Введите символ ')

def count_characters(string, n):
    counter = 0
    for i in string:
        if n == i:
            counter += 1
    return counter

print(count_characters(string, n))