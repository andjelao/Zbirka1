# rastavlja unseni broj na proste cinioce i stampa ih
n = int(input("Unesite vrijednost broja: "))

def rastavljanje_na_proste_cinioce(n):
    djelilac = 2
    while n != 1:
        if n % djelilac == 0:
            print(djelilac, " * ")
            n = n // djelilac
        else:
            djelilac = djelilac + 1
    print(n)
rastavljanje_na_proste_cinioce(n)