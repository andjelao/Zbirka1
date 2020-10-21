# stampa najveci moguci broj koji nastaje kombinacijom cifara unesenog trocifrenog broja
n= int(input("Unesite zeljeni broj: "))

def najveci_broj_kombinacijom_cifara(n):

    prva_cifra = n // 100
    srednja_cifra = (n//10) % 10
    zadnja_cifra = n % 10
    broj = 0

    if prva_cifra > zadnja_cifra:
        if zadnja_cifra > srednja_cifra:
            broj = prva_cifra * 100 + zadnja_cifra * 10 + srednja_cifra
        else:
            if prva_cifra > srednja_cifra:
                broj = prva_cifra * 100 + srednja_cifra * 10 + zadnja_cifra
            else: 
                broj = srednja_cifra * 100 + prva_cifra * 10 + zadnja_cifra
    else:
        if prva_cifra > srednja_cifra:
            broj = zadnja_cifra * 100 + prva_cifra * 10 + srednja_cifra
        else:
            if srednja_cifra > zadnja_cifra:
                broj = srednja_cifra * 100 + zadnja_cifra * 10 + prva_cifra
            else:
                broj = zadnja_cifra * 100 + srednja_cifra * 10 + prva_cifra

    print(broj)

najveci_broj_kombinacijom_cifara(n)