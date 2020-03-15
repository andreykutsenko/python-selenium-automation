
def sum_bn_min_max(array):
    maxi = array[0]
    mini = array[0]
    max_index = 0
    min_index = 0
    index = 0
    while index < len(array):
        if array[index] > maxi:
            maxi = array[index]
            max_index = index
        if array[index] < mini:
            mini = array[index]
            min_index = index
        index += 1
    sub_array = array[min(min_index, max_index) + 1:max(min_index, max_index)]
    result = sum(sub_array)
    return result

print(sum_bn_min_max([1, 1, 111, 2, 5, 6, 7, 33, -532, 9, 7]))