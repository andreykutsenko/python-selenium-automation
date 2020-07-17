from random import randint

def bubble_sort(array):
    for item in range(len(array)):
        j = len(array) - 1
        while j > 0:
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

N = 5
a = []
for i in range(N):
    a.append(randint(1, 99))

print(f'исходный {a}\n')
print(f'отсортированный {bubble_sort(a)}')