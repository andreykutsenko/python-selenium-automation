
def is_isogram(string):
    if len(string) == 0:
        return True
    string = string.upper()
    unic = ''
    for char in string:
        if char in unic:
            return False
        unic += char
    return True

print(is_isogram(''))