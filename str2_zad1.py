# unosenje brojeva dok se ne unese 0, stampa koliko je unesenih pozitivnih a koliko negativnih brojeva

n = int(input("Unesite zeljeni broj: "))

def pozitivni_negativni_brojevi(n):
    broj_pozitivnih = 0
    broj_negativnih = 0
    while n != 0:
        if n > 0:
            broj_pozitivnih = broj_pozitivnih+1
        else:
            broj_negativnih = broj_negativnih+1
        n = int(input("Unesite sljedeci broj: "))
    print("Pozitivnih brojeva ima: ", broj_pozitivnih)
    print("Negativnih brojeva ima: ", broj_negativnih)

pozitivni_negativni_brojevi(n)
