# ispisuje sve brojeve od 100 do 200 koji su djeljivi sa 26
def djeljivi_sa_26():
    for x in range(100, 201):
        if x%26==0:
            print(x)
djeljivi_sa_26()