
def remove_duplicates(array):
    result = []
    for item in array:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates([1, 1, 1, 2, 3, 2, 3]))