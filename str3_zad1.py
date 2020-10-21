# stampa da li je uneseni broj djeljiv sa 3
n = int(input("Unesite zeljeni broj: "))

def djeljiv_sa_3(n):
    if n % 3 == 0:
        print("Broj je djeljiv sa 3. ")
    else:
        print("Broj nije djeljiv sa 3. ")
djeljiv_sa_3(n)