# unosenje broja n, stampa sve savrsene brojeve od 1 do n, savrsen broj- jednak zbiru svih svojih djelilaca iskljucujuci njega samog
n = int(input("Unesite zeljeni broj: "))

def savrseni_brojevi_do_n(n):
    broj = 1
    suma = 0
    djelilac = 1

    while broj <= n:
        while broj % djelilac == 0:
            if broj == djelilac:
                if suma == broj:
                    print(broj)
                suma = 0
                djelilac = 1
                broj = broj + 1 
            else: 
                suma = suma + djelilac
                djelilac = djelilac + 1
        else:
            djelilac = djelilac + 1

savrseni_brojevi_do_n(n)
    