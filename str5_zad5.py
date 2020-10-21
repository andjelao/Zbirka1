#ispisuje trocifrene brojeve kod kojih su prva i zadnja cifra jednake
def jednaka_prva_i_zadnja_cifra():
  broj=100
  while broj<=999:
      zadnja_cifra=broj%10
      prva_cifra=broj//100
      if zadnja_cifra==prva_cifra:
        print(broj)
      broj=broj+1
jednaka_prva_i_zadnja_cifra()         
    
