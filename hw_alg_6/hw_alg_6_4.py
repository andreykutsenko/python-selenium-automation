# Найти максимальный элемент среди минимальных элементов столбцов матрицы

def max_in_min_elem_columns_matrix_without_col(matrix):
    min_column = []
    for i in range(len(matrix[0])):
        result = []
        for j in range(len(matrix)):
            result.append(matrix[j][i])
        min_column.append(min(result))
    return f'Max element is {max(min_column)}'

# print(max_in_min_elem_columns_matrix_without_col([[-1,-2, -3], [-4, 5, 6], [7, 8, 9]]))


def max_in_min_elem_columns_matrix(matrix):
    result_min = {}
    result_col = {}
    for i in range(len(matrix[0])):
        result = []
        for j in range(len(matrix)):
            result.append(matrix[j][i])
        # создаем 2 словаря
        # словарь, где ключи - номера столбцов
        result_min[i] = min(result)
        # словарь, где ключи - мин-е эл-ты
        result_col[min(result)] = i
    # print(result_min)
    # print(result_col)
    return f'Максимальный элемент среди минимальных элементов столбцов: {max(result_min.values())} \nв столбце N {result_col.get(max(result_min.values())) + 1}'

# print(max_in_min_elem_columns_matrix([[1, 200, 3], [4, 5, 6], [7, 8, 9]]))
print(max_in_min_elem_columns_matrix([[-1, -22, -3], [-4, 5, 6], [7, 8, 9]]))