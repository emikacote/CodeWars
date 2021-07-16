def factorial(n):
    if n>12 or n<0: raise ValueError
    return 1 if n <=1 else n*factorial(n-1)
