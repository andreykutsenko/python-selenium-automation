# str = input(f'Введите строку текста ')

def reverse_str(str):
    # return str[::-1]
    # return ''.join(reversed(str))
    result = ''
    index = len(str)
    while index > 0:
        result += str[index-1]
        index -= 1
    return result


# print(reverse_str(str))