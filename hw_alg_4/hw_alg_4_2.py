string = input(f'Введите строку ')
sub_str_s = input(f'Введите подстроку для поиска ')
sub_str_r = input(f'Введите подстроку для замены ')

def replace_string(string, sub_str, sub_str_r):
    new_string = 'Строка не изменилась'
    if sub_str_s in string:
        A = string.split(sub_str_s)
        new_string = sub_str_r.join(A)
    return new_string

print(replace_string(string, sub_str_s, sub_str_r))