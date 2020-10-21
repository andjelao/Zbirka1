# stampa kvadrat unesenog broja ako je negativan, a ako je pozitivan njegovu dvostruku vrijednost
n = int(input("Unesite zeljeni broj: "))

def kvadrat_i_dvostruka_vrijednost(n):
    if n > 0:
        n = 2 * n
    else:
        n = n ** 2
    print(n)
kvadrat_i_dvostruka_vrijednost(n)
