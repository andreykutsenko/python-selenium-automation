import random

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        ran_element = random.choice(array)
        small_array = []
        equal_array = []
        greater_array = []
        for n in array:
            if n < ran_element:
                small_array.append(n)
            elif n == ran_element:
                equal_array.append(n)
            else:
                greater_array.append(n)
        return quick_sort(small_array) + quick_sort(equal_array) + quick_sort(greater_array)
#
# N = 10
# a = []
# for i in range(N):
#     a.append(random.randint(1, 99))
#
# print(f'исходный {a}\n')
print(f'отсортированный {quick_sort([5,2,1])}')