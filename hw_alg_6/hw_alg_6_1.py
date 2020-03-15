# Дан лист. Вернуть лист, состоящий из элементов, которые меньше среднего арифметического исходного листа.
# С.а. = сумма элементов разделить на количество.

def arr_less_average(arr):
    result = []
    avr = sum(arr) / len(arr)
    for i in arr:
        if i < avr:
            result.append(i)
    return result

print(arr_less_average([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))