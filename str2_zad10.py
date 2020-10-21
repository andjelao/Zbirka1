# unosenje brojeva dok se ne unese 0, stampa koliko unesenih brojeva ima barem jednu parnu cifru
n = int(input("Unesite broj: "))

def barem_jedna_parna_cifra(n):
    brojac= 0
    while n != 0:
        parne_cifre = 0
        while n > 0:
            if parne_cifre < 1:
                cifra = n % 10
                if cifra % 2 == 0:
                    parne_cifre = parne_cifre + 1
                    brojac = brojac + 1
                n = n // 10
            else:
                break
        n = int(input("Unesite broj: "))
    print(brojac)

barem_jedna_parna_cifra(n)