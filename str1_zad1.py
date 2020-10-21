# stampa da li je srednja cifra unesenog trocifrenog broja parna, neparna ili nula

n = int(input("Unesite zeljeni broj: "))

def srednja_cifra_parna_neparna_nula(n):
    srednja_cifra = (n // 10) % 10

    if srednja_cifra == 0:
        print("Srednja cifra je nula.")
    elif srednja_cifra % 2 == 0:
        print("Srednja cifra je parna.")
    elif srednja_cifra % 2 == 1:
        print("Srednja cifra je neparna.")

srednja_cifra_parna_neparna_nula(n)