
def split_in_half(string):
    string_len = len(string)
    half = int(string_len / 2)
    if string_len % 2 == 0:
        first = string[:half]
        second = string[half:]
    else:
        first = string[:half+1]
        second = string[half+1:]
    return f'{second}{first}'

print(split_in_half('Hello!!'))