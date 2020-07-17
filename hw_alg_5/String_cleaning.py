
def string_cleaning(string):
    result = ''
    for char in string:
        if not char.isdigit():
            result += char
    return result

print(string_cleaning('wgfrweg89fgf98fdgdfgdfg76fdgfd8'))

# def change(st):
#     if st = '    ':
#         result = '00010111000000000001000010'
#     else:
#         lit = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         nm_l = list("00000000000000000000000000")
#         for i in list(st.upper()):
#             if i in lit:
#                 nm_l[lit.index(i)] = '1'
#         result = ''.join(nm_l)
#     return result
#
# print(change('2387643284823647823   98798   987987 abc'))