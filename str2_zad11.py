# unosenje brojeva dok se ne unese nula, stampa koliko njih ima tacno jednu neparnu cifru
n = int(input("Unesite broj: "))

def tacno_jedna_neparna_cifra(n):
    brojac = 0
    while n != 0:
        neparne_cifre = 0
        while n > 0:
            cifra = n % 10
            if cifra % 2 == 1:
                neparne_cifre = neparne_cifre + 1
            n = n // 10
        if neparne_cifre == 1:
            brojac = brojac + 1
        n = int(input("Unesite broj: "))
        
    print(brojac)
tacno_jedna_neparna_cifra(n)            

