
length = int(input(f"Введите длину массива: "))
array = []

for item in range(length):
    number = int(input(f"Введите элемент массива: "))
    array.append(number)

def sum_and_mult(array):
    summ = 0
    mult = 1
    for item in array:
        summ += item
        mult *= item
    return {
        "summ": summ,
        "mult": mult,
        "array": array
    }

print(sum_and_mult(array))