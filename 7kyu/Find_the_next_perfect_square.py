from math import sqrt, trunc

def find_next_square(sq):
    num = sqrt(sq)
    if sq == 0:
        return 1
    try:
        assert sq%num == 0
    except:
        return -1
    if True:
        num += 1
        num *= num
        return trunc(num)
