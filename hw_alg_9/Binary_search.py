import random

def binary_search(array, item):
    first = 0
    last = len(array) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if item == array[mid]:
            found = True
        elif item < array[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return found



N = 50
a = []
for i in range(N):
    a.append(random.randint(1, 99))
a.sort()
print(f'исходный {a}\n')
print(f'{binary_search(a, 99)}')
