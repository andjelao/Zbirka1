# stampa najmanju cifru unesenog broja
n = int(input("Unesite zeljeni broj: "))

def najmanja_cifra(n):
    najmanja_cifra = n % 10
    n = n // 10
    while n > 0:
        cifra = n % 10
        n = n// 10
        if(cifra < najmanja_cifra):
            najmanja_cifra = cifra
    print("Najmanja cifra je: ", najmanja_cifra)
najmanja_cifra(n)