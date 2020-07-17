
def square_sum(array):
    result = []
    for item in array:
        result.append(item ** 2)
    return sum(result)


print(square_sum([1, 2, 2]))