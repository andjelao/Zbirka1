# sabiranje/oduzimanje/ mnozenje unesena dva razlomka

print("Unesite prvi razlomak: ")
brojilac1 = int(input("brojilac: "))
imenilac1 = int(input("imenilac: "))

print("Unesite drugi brojilac: ")
brojilac2 = int(input("brojilac: "))
imenilac2 = int(input("imenilac: "))
operacija = int(input("Unesite broj odgovarajuce racunske operacije: 1-sabiranje, 2- oduzimanje, 3- mnozenje: "))

def operacije_sa_razlomcima(brojilac1, imenilac1, brojilac2, imenilac2, operacija):
    brojilac = 0
    imenilac = imenilac1 * imenilac2
    if operacija == 1:
        brojilac= brojilac1 * imenilac2 + brojilac2 * imenilac1
    elif operacija == 2:
        brojilac = brojilac1 * imenilac2 - brojilac2 * imenilac1
    elif operacija == 3:
        brojilac = brojilac1 * brojilac2
    else:
        print("Pogresna operacija! ")

    print(brojilac, "/", imenilac)

operacije_sa_razlomcima(brojilac1, imenilac1, brojilac2, imenilac2, operacija)
