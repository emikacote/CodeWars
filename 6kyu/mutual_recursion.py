f,m =(lambda n: n-m(f(n-1)) if n else 1, lambda n: n-f(m(n-1)) if n else 0)
