# unosenje datuma u obliku dd.mm.gg, stampa datum sa imenom mjeseca umjesto broja
datum= input(" Unesite datum u formatu dan.mjesec.godina: ")

prva_tacka=datum.index(".")
zadnja_tacka=datum.rfind(".")
druga_tacka= datum.find(".", prva_tacka+1, zadnja_tacka)

mjesec= datum[prva_tacka+1 : druga_tacka]
dan= datum[0 : prva_tacka+1]
godina= datum[druga_tacka+1: zadnja_tacka+1]

if mjesec=="1":
    mjesec= "januar"
elif mjesec=="2":
    mjesec="februar"
elif mjesec== "3":
    mjesec= "mart"
elif mjesec== "4":
    mjesec= "april"
elif mjesec== "5":
    mjesec= "maj"
elif mjesec=="6":
    mjesec="jun"
elif mjesec=="7":
    mjesec="jul"
elif mjesec=="8":
    mjesec="avgust"
elif mjesec=="9":
    mjesec="septembar"
elif mjesec=="10":
    mjesec="oktobar"
elif mjesec=="11":
    mjesec= "novembar"
else: 
    mjesec= "decembar"

print(dan, mjesec, godina)



    

