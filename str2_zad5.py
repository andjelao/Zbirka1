# stampa koliko ima cetvorocifrenih brojeva ciji je zbir prve i cetvrte cifre jednak proizvodu druge  trece

def cetvorocifreni_brojevi_zbir_i_proizvod_cifara():
    broj = 1000
    prva_cifra = 0
    druga_cifra = 0
    treca_cifra = 0
    cetvrta_cifra = 0
    brojac = 0

    while broj <= 9999:
        prva_cifra = broj // 1000
        cetvrta_cifra = broj % 10
        druga_cifra = (broj // 100) % 10
        treca_cifra = (broj // 10) % 10

        if prva_cifra + cetvrta_cifra == druga_cifra * treca_cifra:
            brojac= brojac + 1
        
        broj= broj + 1

    print(brojac, "brojeva")
    
cetvorocifreni_brojevi_zbir_i_proizvod_cifara()