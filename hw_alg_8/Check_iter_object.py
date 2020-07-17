
def check_iter(maybe_iterable):
    try:
        iter(maybe_iterable)
        print('iteration will probably work')
    except TypeError:
        print('not iterable')

check_iter(345)
