# str = input(f'Введите строку текста ')
#
# def reverse_str(str):
#     # return str[::-1]
#     # return ''.join(reversed(str))
#     result = ''
#     index = len()
#     while index > 0:
#         result += str[index-1]
#         index -= 1
#     return result


# print(reverse_str(str))


def descending_order(num):
    num_l = []
    for i in range(len(str(num))):
        num_l.append(int(list(str(num))[i]))
    return int("".join(map(str, sorted(num_l)[::-1])))

print(descending_order(51234567980))