# stampa korijen najvece cifre unesenog trocifrenog broja
import math

n = int(input("Unesite zeljeni broj: "))

def korijen_najvece_cifre(n):
    najveca_cifra = n % 10
    n= n // 10
    while n > 0:
        cifra = n % 10
        n= n // 10
        if cifra > najveca_cifra:
            najveca_cifra = cifra

    najveca_cifra = int(math.sqrt(najveca_cifra))
    print("Korijen najvece cifre je:", najveca_cifra)

korijen_najvece_cifre(n)