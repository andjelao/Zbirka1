# for petljom omoguciti unos temperature za sedam dana u nedelji, zatim izracunati i ispisati prosjecnu temperaturu
def prosjecna_temperatura():
    suma_temperatura=0
    prosjecna_temperatura=0
    for x in range(7):
        t=int(input("Unesite temperaturu: "))
        suma_temperatura= suma_temperatura + t
    prosjecna_temperatura= suma_temperatura / 7
    print("Prosjecna temperatura za ovu sedmicu je: ", prosjecna_temperatura)
prosjecna_temperatura()