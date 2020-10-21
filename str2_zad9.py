# stampa n za koje vrijedi da je 1*2*3*...*n=3628800

def vrijednost_n():
    n = 1
    proizvod = 1

    proizvod = proizvod * n
    while proizvod != 3628800:
        n = n + 1
        proizvod = proizvod * n
    print(n)

vrijednost_n()