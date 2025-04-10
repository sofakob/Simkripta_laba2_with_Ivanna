from gcd import gcd
from algoritm_evklida import algoritm_evklida_with_a_b
def porivniia(a:int, b:int, n:int):
    d=gcd(a, n)
    print(d)
    if d==1:
        x=algoritm_evklida_with_a_b(a, n)*b
        return x
    elif d>1:
        if b%d!=0:
            return 
        else:
            arr_rozviazki=[]
            a1=a/d; b1=b/d; n1=n/d
            x0=b1*algoritm_evklida_with_a_b(a1, n1)
            arr_rozviazki.append(x0)
            for i in range(d):
                x0+=n1
                arr_rozviazki.append(x0)
            return arr_rozviazki
        


print(porivniia(33, 6, 72))


        
        