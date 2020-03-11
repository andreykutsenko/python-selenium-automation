
def no_duplicate(string):
    array = string.split(' ')
    result = []
    for item in array:
        if not item in result:
            result.append(item)
    return ' '.join(result)

print(no_duplicate('dfd qwerty kjhkl qwerty'))