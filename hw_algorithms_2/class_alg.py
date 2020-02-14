# import math
from random import randint

# --- Factorial ---
# a = int(input('Введите число '))
# b = int(input('Введите число '))
# print(f'a={a}, b={b}')
# a, b = b, a
# print(f'a={a}, b={b}

# n = int(input("Введите число для расчета факториала: "))
#
# def factorial(n):
#     return math.factorial(n)
#
# print(factorial(n))

#  --- Sum of three-digit numbers ---
# n = randint(100,999)
# print(f'мы получили случайное 3-х значное число: {n}')
# one = n % 10
# print(f'последнее число = {one}')
# two = n // 10 % 10
# print(f'второе число = {two}')
# tr = n // 100
# print(f'первое число = {tr}')
# sum = one+two+tr
# print(f'сумма чисел = {sum}')


#  --- Leap year ---
# year = int(input('Введите год '))
#
# if year % 4 != 0:
#     print('Не високосный')
# else:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Високосный')
#         else:
#             print('Не високосный')
#     else:
#         print('Високосный')

#  --- Binary gap ---
# n = int(input('Введите число '))
#
# def to_bin(n):
#     bin_string = ''
#     while n > 0:
#         bin_string += str(n % 2)
#         n = n // 2
#     return bin_string[::-1]
#
# def binary_gap(n):
#     n = to_bin(n)
#     max_gap = 0
#     counter = 0
#     # bin_gap = False
#     for item in n:
#         if item == '1':
#             # bin_gap = False
#             if max_gap < counter:
#                 max_gap = counter
#             counter = 0
#         else:
#             counter += 1
#             # bin_gap = True
#
#     print(max_gap)
#     return n
#
# # print(binary_gap(n))
#
# print(bin(n))