# n - count discs, i - first pen, k - target pen, (6-i-k) - tmp pen

# def hanoi(n, i, k):
#     if n == 1:
#         print(f'Move disk 1 from N{i} to N{k}')
#     else:
#         tmp_pen = 6 - i - k
#         hanoi(n - 1, i, tmp_pen)
#         print(f'Move disk #{n} from N{i} to N{k}')
#         hanoi(n - 1, tmp_pen, k)
#     return 0

# def hanoi_Arr(n):
#
#     i = list(range(n,0,-1))
#     k = []
#     tmp = []
#
#
#     if n == 1:
#         k.append(i[0])
#         print(f'[{i}, {k}, {tmp}]\n')
#     else:
#         # count = len(i) - 1
#         tmp.append(hanoi_Arr(n-1))
#         print(f'[{i}, {k}, []]\n')
#         k.append(hanoi_Arr(n-1))
#         print(f'[{i}, {k}, {tmp}]\n')
#     return 0


# print(hanoi(5, 1, 2))

# print((hanoi_Arr(3)))


def max_diff(lst):
    print(len(lst))
    if len(lst) > 0:
        result = max(lst) - min(lst)
    result = 0
    return result


print(max_diff([-1, 2, 3]))

