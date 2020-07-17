from random import randint

def insertion_sort(array):
    print(range(len(array)))
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

N = 5
a = []
for i in range(N):
    a.append(randint(1, 99))

print(f'исходный {a}\n')
print(f'отсортированный {insertion_sort([a])}')