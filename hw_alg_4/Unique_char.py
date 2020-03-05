string = input(f'Введите буквы : ')


def unique_char(string):
    result = ''
    for i in string:
        if i not in result:
            result += i
    return result

def unique_char_t(string):
    result = ''
    for item in string:
        if result.count(item) == 0:
            result += item
    return result


print(unique_char(string))