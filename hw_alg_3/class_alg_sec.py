def secondes_to_date (sec):
    count_h = sec // 3600
    count_m = (sec // 60) % 60
    count_s = sec % 60
    # return print(f'HH:MM:SS -> {count_h}:{count_m}:{count_s}')
    return "%02d:%02d:%02d" % (count_h, count_m, count_s)

print (secondes_to_date(3975))