# rastaviti uneseni pozitivni cijeli broj na dva dijela tako da njihov proizvod bude minimalan

n = int(input("Unesite zeljeni broj: "))
def minimalan_proizvod_djelova_broja(n):
    cifra = 0
    pozicija = 0 
    proizvod = 0
    najmanji_proizvod = 0
    najmanjin = 0
    najmanjac = 0

    while n > 9:
        cifra = (n % 10) * 10 ** pozicija + cifra
        n = n // 10
        proizvod = cifra * n

        if pozicija == 0:
            najmanji_proizvod = proizvod + 1
            
        pozicija = pozicija + 1

        if proizvod < najmanji_proizvod:
            najmanji_proizvod = proizvod
            najmanjin = n
            najmanjac = cifra

    print(najmanjin, najmanjac)
minimalan_proizvod_djelova_broja(n)  
