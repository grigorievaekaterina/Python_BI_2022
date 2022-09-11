def add(a, b):
    return a + b

def sum(lst):
    s = 0
    for item in lst:
        s = add(s, item)
    return s