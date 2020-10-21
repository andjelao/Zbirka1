#ispisuje sve dvocifrene parne brojeve
def dvocifreni_parni_brojevi():
    broj=10
    while broj<100:
        if(broj%2==0):
            print(broj)
        broj=broj+1
dvocifreni_parni_brojevi()