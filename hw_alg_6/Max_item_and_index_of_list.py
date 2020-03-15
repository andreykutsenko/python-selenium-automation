
from random import randint

length = int(input(f"Введите длину массива: "))
array = []

for item in range(length):
    number = randint(-100, 100)
    array.append(number)

print(array)

def max_item_and_index_of_list(array):
    max = array[0]
    max_index = 0
    index = 0
    while index < len(array):
        if array[index] > max:
            max = array[index]
            max_index = index
        index += 1
    return {
        "maximum": max,
        "max_index": max_index
    }

print(max_item_and_index_of_list(array))