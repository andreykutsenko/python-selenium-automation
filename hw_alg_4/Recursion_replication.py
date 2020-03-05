string = input(f'Введите строку ')
n = int(input(f'Введите число повторений '))

def recursive_replication(string, n):
    if n > 1:
        return recursive_replication(string, n-1) + string
    elif n == 1:
        return string

print(recursive_replication(string, n))