import numpy as np
def max_sequence(arr):
    new = []
    if not arr: return 0
        if max(arr) <= 0: return 0
        n = 0
        while n <= len(arr):
            for i in range(len(arr)+1):
                if n < i:
                    a = np.sum(arr[0+n:i])
                    print(a)
                        new.append(a)
                        b = np.sum(arr[i:0-n])
                        print(b)
                            new.append(b)
                n+=1

    return max(new)
