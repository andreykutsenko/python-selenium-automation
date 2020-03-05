def str_decompression(string):
    new_string = ''
    for i in range(len(string)):
        if string[i].isdigit():
            counter = int(string[i])
            new_string = new_string + string[i-1] * counter
        elif i == len(string)-1:
            new_string = new_string + string[i]
    return new_string

print(str_decompression('а4б3в2г'))