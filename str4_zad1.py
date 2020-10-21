# stampa koliko nula ima faktorijal unesenog broja
n = int(input("Unesite vrijednost broja: "))

def broj_nula_faktorijala(n):
    faktorijal = 1
    broj_nula = 0

    while n > 0:
        faktorijal = faktorijal * n
        n = n - 1

    while faktorijal > 0:
        if faktorijal % 10 == 0:
            broj_nula = broj_nula + 1
        faktorijal = faktorijal // 10
    print("Faktorijal ima ", broj_nula, " nula. ")
broj_nula_faktorijala(n)