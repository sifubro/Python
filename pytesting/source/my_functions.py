def add(x,y):
    return x+y


def divide(x,y):
    return x/y


def divide_custom_raise(x,y):
    if y == 0:
        raise ValueError
    return x / y