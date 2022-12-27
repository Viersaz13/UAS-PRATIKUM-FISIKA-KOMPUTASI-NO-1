from trapezoid import*

def f(x):
    return x**3

n = int(100)
a = float(input('batas bawah = '))
b = float(input('batas atas = '))

integral = trapezoid(f,a,b,n)

print('integral =', integral)
