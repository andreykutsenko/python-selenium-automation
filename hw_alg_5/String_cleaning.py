
def string_cleaning(string):
    result = ''
    for char in string:
        if not char.isdigit():
            result += char
    return result

print(string_cleaning('wgfrweg89fgf98fdgdfgdfg76fdgfd8'))

