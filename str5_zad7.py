# suma prvih 20 prirodnih brojeva

def suma_prvih_20_prirodnih_brojeva(n):
    broj=1
    suma=0
    while broj<=n:
        suma=suma+broj
        broj=broj+1

    print(suma)

suma_prvih_20_prirodnih_brojeva(20)
 