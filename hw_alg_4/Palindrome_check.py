from Reverse_str import reverse_str

str = input(f'Введите строку ')

def palindrome_check(str):
    if str == reverse_str(str):
        return True
    else:
        return False

print(palindrome_check(str))