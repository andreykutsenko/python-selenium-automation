# def multiplication(number_1, number_2):
#     iterator = 0
#     result = 0
#     while iterator < number_2:
#         result += number_1
#         iterator += 1
#     return result
#
# print(multiplication(7,8))


# def multiplication(n):
#     count = 0
#     n = str(n)
#     while len(n) > 1:
#         p = 1
#         for i in n:
#             p *= int(i)
#         n = str(p)
#         count += 1
#     return count
#
# print(multiplication(1))


# def longest(s1, s2):
#     s = 'abcdefghijklmnopqrstuvwxyz'
#     s3 = s1 + s2
#     s0 = ''
#     for i in s:
#         if i in s3:
#             # print(i)
#             s0 += i
#     return s0
#
# print(longest("aretheyhere", "yestheyarehere"))


def get_strings(city):
    city = city.lower()
    l = ''
    for i in city:
        if i in l:
            pass
        elif i == ' ':
            pass
        else:
            l += i + ':' + ('*' * city.count(i)) + ','
    return l[:-1]


print(get_strings("Chicago"))