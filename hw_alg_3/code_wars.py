# Find the odd int
# Given an array, find the integer that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

# def find_it(seq):
#     counter = {}
#     for item in seq:
#         counter[item] = counter.get(item, 0) + 1
#     odd = {item for item, count in counter.items() if count % 2 != 0}
#     return print(list(odd)[0])
#
# find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
#
#
# # perfect solution
# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i


# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")


# def get_middle(s):
#     m = len(s) // 2
#     k = 0
#     if len(s) % 2 == 0: k = 1
#     return print(s[m - k:m+1])
#
#        #your code here
#
# get_middle("middle")


# def accum(s):
#     i = 0
#     m = ''
#     while i < len(s):
#         m += (s[i]*(i+1)).capitalize()
#         i += 1
#         if i < len(s): m += '-'
#     return print(m)
#
# accum("ZpglnRxqenU")


def remove(s):
    s = s[::-1]
    result = ''
    t = 1
    for i in range(len(s)):
        if s[i] == '!' and t == i+1:
            result += s[i]
            t += 1
    result = result + s[t-1:].replace('!','')
    return print (result[::-1])

# remove('!Hi!!!')
remove('!Hi! Hi!!!')