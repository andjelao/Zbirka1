# provjerava da li je broj prost
n = int(input("Unesite zeljeni broj: "))

def prost_broj(n):
    djelilac = 2
    while(n % djelilac != 0):
        djelilac = djelilac + 1
    if(n == djelilac):
        print("Broj je prost.")
    else:
        print("Broj nije prost")
prost_broj(n)