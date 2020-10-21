# trazi od korisnika unos 2 broja, korisnik bira zeljenu operaciju i stampa se rezultat te operacije

print("Unesite dva broja: ")
a = int(input("a: "))
b = int(input("b: "))
broj_operacije = int(input("Unesite broj zeljene operacije: 1-sabiranje 2- oduzimanje 3- proizvod 4-kolicnik : "))

def operacija_dva_broja(a, b, broj_operacije):
    rezultat = 0
    if broj_operacije == 1:
        rezultat = a + b
    elif broj_operacije == 2:
        rezultat = a - b
    elif broj_operacije == 3:
        rezultat = a * b
    elif broj_operacije == 4:
        rezultat = a / b
    else: 
        print("Pogresna operacija! ")
    print(rezultat)
operacija_dva_broja(a, b, broj_operacije)