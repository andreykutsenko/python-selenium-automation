# Вводится ненормированная строка, у которой могут быть пробелы в начале,
# в конце и между словами более одного пробела.
# Привести ее к нормированному виду, т.е. удалить все пробелы в начале и конце,
# а между словами оставить только один пробел.

string = input('Введите предложение: ')

def del_gap(string):
    array = string.strip().split(' ')
    result = []
    for item in array:
        if len(item) > 0:
            result.append(item)
    return ' '.join(result)

print(del_gap(string))