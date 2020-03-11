
def help_bob(string):
    result = ''
    for char in string:
        if char.isdigit() or char.isalpha():
            result += char
    # print(result)
    return len(result)


print(help_bob("!2jh$%#%3g"))