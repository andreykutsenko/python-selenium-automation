
def pair_sum(arr, k):
    result = []
    i = 0
    while i < len(arr):
        ii = 0
        while ii < len(arr):
            if arr[i] + arr[ii] == k and i != ii:
                find = sorted([arr[i], arr[ii]])
                if find not in result:
                    result.append(find)
            ii += 1
        i += 1
    return result

print(pair_sum([1, 3, 3, 2, 4, -1, 5], 6))
