# stampa aritmeticku sredinu trocifrenih brojeva kojima je zadnja cifra 5, a zbir cifara je 15

def aritmeticka_sredina():
    broj = 100
    suma_brojeva = 0
    brojac = 0
    suma_cifara = 0
    i = 0
    aritmeticka_sredina = 0

    while broj <= 999:
        i = broj
        suma_cifara = 0
        if i % 10 == 5:
            while i > 0:
                cifra = i % 10
                i = i // 10
                suma_cifara = suma_cifara + cifra  
            if suma_cifara == 15:
                suma_brojeva = suma_brojeva + broj
                brojac = brojac + 1
        broj = broj + 1

    aritmeticka_sredina = suma_brojeva / brojac
    print("Aritmeticka sredina je: ", aritmeticka_sredina)

aritmeticka_sredina()

    