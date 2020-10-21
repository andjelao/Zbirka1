# stampa rezultat i ostatak cjelobrojnog dijeljenja dva unijeta cijela broja, koristeci samo operacije sabiranja i oduzimanja

print("Unesite dva cijela broja: ")
a = int(input("a: "))
b = int(input("b: "))

def rezultat_i_ostatak_dijeljenja(a,b):
    rezultat = 0
    ostatak = a - b
    while ostatak >= 0: 
        rezultat = rezultat + 1
        ostatak = ostatak - b
    ostatak = ostatak + b
    print("Rezultat cjelobrojnog dijeljenja ", a, " i ", b, "je: ", rezultat)
    print("Ostatak cjelobrojnog dijeljenja ", a, " i ", b, "je: ", ostatak)
    
rezultat_i_ostatak_dijeljenja(a,b)
