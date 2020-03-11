import math

def f(x):
    return x**3-x-2

tol = 10**-6

def bisection(function, a, b):
    iters = math.ceil(math.log((b-a)/tol,2))
    if f(a)*f(b)<=0:
        for i in range(iters):
            c = (a+b)/2
            if f(c)/abs(f(c)) == f(a)/abs(f(a)):
                a=c
            else:
                b=c
    return c


root = bisection(f, 0, 2)
print(root)
