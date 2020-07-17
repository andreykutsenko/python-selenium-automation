
def sum_sublist(array):
    best_sum = 0
    current_sum = 0
    for item in array:
        current_sum += item
        if current_sum < 0:
            current_sum = 0
        else:
            if current_sum > best_sum:
                best_sum = current_sum
    return best_sum


print(sum_sublist([5, 4, -3, 4, -9, 2, -6]))