def factorial(n):
    if n<0: return None
    return n*factorial(n-1) if n>1 else 1
  
# Or using recursive lambda function for one-liner:

factorial = lambda n: None if n<0 else n*factorial(n-1) if n>1 else 1
