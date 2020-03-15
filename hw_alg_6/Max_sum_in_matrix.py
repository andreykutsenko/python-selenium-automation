
# def max_sum_in_matrix(matrix):
    # For rows
    # maximum = 0
    # max_row = 0
    # row = 1
    # for item in matrix:
    #     summ = 0
    #     for element in item:
    #         summ += element
    #     if summ > maximum:
    #         maximum = summ
    #         max_row = row
    #     row += 1
    # return f'Row with max sum is {max_row}'

    # For columns

    # return

def max_sum_in_matrix1(matrix):
    result_sum = {}
    result_col = {}
    for i in range(len(matrix[0])):
        sum = 0
        # 'пробегаем' по строкам i-го столбца
        for j in range(len(matrix)):
            sum += matrix[j][i]
        # создаем 2 словаря
        # словарь с ключами номеров столбцов
        result_sum[i] = sum
        # словарь с ключами сумм
        result_col[sum] = i
    return f'Максимальная сумма {max(result_sum.values())} в столбце N {result_col.get(max(result_sum.values())) + 1}'

print(max_sum_in_matrix1([[1, 200, 3], [4, 5, 6], [7, 8, 9]]))