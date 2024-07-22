from math import inf

def devide(first, second):
    for i in first, second:
        if i == 0:
            return inf
    return first / second
