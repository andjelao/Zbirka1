# unosenje datuma u obliku dd.mm.gg, stampa datum sa imenom mjeseca umjesto broja
datum = input(" Unesite datum u formatu dd.mm.gg. : ")

def formatiraj_datum(datum):
    datum = datum.split(".")
    dan = datum[0]
    mjesec = datum[1]
    godina = datum[2]

    if mjesec == "01":
        mjesec = "januar"
    elif mjesec == "02":
        mjesec = "februar"
    elif mjesec == "03":
        mjesec = "mart"
    elif mjesec == "04":
        mjesec = "april"
    elif mjesec == "05":
        mjesec= "maj"
    elif mjesec == "06":
        mjesec = "jun"
    elif mjesec =="07":
        mjesec = "jul"
    elif mjesec =="08":
        mjesec = "avgust"
    elif mjesec == "09":
        mjesec = "septembar"
    elif mjesec =="10":
        mjesec = "oktobar"
    elif mjesec == "11":
        mjesec = "novembar"
    else: 
        mjesec = "decembar"

    print(dan + ". " + mjesec + " " + godina + ".")

formatiraj_datum(datum)
