# provjerava da li je uneseni broj potpuno paran- svaka cifra broja mora da bude parna
n= int(input("Unesite zeljeni broj: "))

def potpuno_paran_broj(n):
    while n>0:
        cifra=n%10
        n=n//10
        if(cifra%2!=0):
            print("Broj nije potpuno paran.")
            break
    else:
        print("Broj je potpuno paran.")

potpuno_paran_broj(n)