# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

def two_min(array):
    result = [min(array)]
    i = 0
    while i < len(array):
        if array[i] <= min(result) \
                and i != array.index(min(array)) \
                and len(result) < 2:
            result.append(array[i])
        i += 1
    return result

print(two_min([0, 1, 3, 1, -7, 2, 0, -6, -7, -7]))

