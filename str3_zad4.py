# za unesene koeficijente kvadratne jednacine stampa njena rjesenja
import math
import cmath
print("Unesite koeficijente kvadratne jednacine: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def kvadratna_jednacina(a, b, c):
    d= b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(b**2 - 4*a*c )) / 2*a
        x2 = (-b - math.sqrt(b **2 - 4*a*c )) / 2*a
        print(x1)
        print(x2)
    elif d == 0:
        x= -b / 2 * a
        print(x)
    else:
        x1 = (-b + cmath.sqrt(b**2 - 4*a*c )) / 2*a
        x2 = (-b - cmath.sqrt(b**2 - 4*a*c )) / 2*a
        print(x1)
        print(x2)
kvadratna_jednacina(a,b,c)
