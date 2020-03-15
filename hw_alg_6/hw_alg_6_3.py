# Найти максимальный элемент среди минимальных элементов строк матрицы.

def min_to_max(matrix):
    min_row = []
    for item in matrix:
        min_row.append(min(item))
    return f'Max element is {max(min_row)}'

print(min_to_max([[1, 2, 3], [4, 5, 6], [100, -800, 99]]))