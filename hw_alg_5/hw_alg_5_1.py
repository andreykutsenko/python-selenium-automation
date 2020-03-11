# В строке, состоящей из слов, разделенных пробелом, найти самое длинное слово.
# Строка вводится с клавиатуры.

string = input('Введите слова через пробел: ')

def long_substr(string):
    array = string.split(' ')
    result = ''
    for item in array:
        if len(item) > len(result):
            result = item
    return f'Длинное слово: {result}'

print(long_substr(string))