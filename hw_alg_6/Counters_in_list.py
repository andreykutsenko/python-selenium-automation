
def counters_in_list(array):
    positive = 0
    negative = 0
    null = 0
    for item in array:
        if item > 0:
            positive += 1
        elif item == 0:
            null += 1
        else:
            negative += 1
    return {
        "positive": positive,
        "negative": negative,
        "null": null
    }

print(counters_in_list([1, -1, 0, 5, -5, 0, 1, 2, -3]))