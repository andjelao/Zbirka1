# za unesene koeficijente ka=vadratne jednacine stampa njena rjesenja
import math
import cmath
print("Unesite koeficijente kvadratne jednacine: ")
a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))

try:   #domen za sqrt je od nula do beskonacno
    x1= (-b+ math.sqrt(b**2-4*a*c )) / 2*a
    x2= (-b- math.sqrt(b**2-4*a*c )) / 2*a
except:  # izuzetak ako je korijen negativan- kompleksan broj
    x1= (-b+ cmath.sqrt(b**2-4*a*c )) / 2*a
    x2= (-b- cmath.sqrt(b**2-4*a*c )) / 2*a
print(x1 , x2)