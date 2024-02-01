def add(x,y):
    return x+y

def divide(x,y):
    if y==0:
        raise ValueError("y should be non zero")
    return x/y