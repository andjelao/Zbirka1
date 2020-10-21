# unose se brojevi dok se ne unese broj djeljiv sa 3, stampa aritmeticku sredinu koja ukljucuje i poslednji broj
n = int(input("Unesite zeljeni broj: "))

def aritmeticka_sredina_djeljivi_sa_3(n): 
  suma = 0
  brojac = 0
  while n % 3 != 0:
    suma = suma + n
    brojac = brojac + 1
    n = int(input("Unesite sljedeci broj: "))
  suma = suma + n
  brojac = brojac + 1
  aritmeticka_sredina = suma / brojac
  print("Aritmeticka sredina unesenih brojeva je: ", aritmeticka_sredina)

aritmeticka_sredina_djeljivi_sa_3(n)