# stampa sve kombinacije cifara a i b za koje vazi da je a*a^b= a*b*b*a

def kombinacije_cifara_za_uslov_a_i_b():
    a=0
    b= 0
    while a!=10:
        if a * a**b == a*b*b*a:
            print(a, b)

        if b<9:
            b=b+1
        else:
            b=0
            a=a+1
      
kombinacije_cifara_za_uslov_a_i_b()