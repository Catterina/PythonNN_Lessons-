#a*x**2+b*x+c =0

def kvadr(a,b,c):
    D = b ** 2 - 4 * a * c
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    return x1, x2

x1, x2 =kvadr(2, 2, -3)
print(x1, x2)