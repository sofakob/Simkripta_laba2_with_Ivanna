from gcd import gcd
from algoritm_evklida import algoritm_evklida_with_a_b


def porivniia(a:int, b:int, n:int):
    '''
    Функція що розв'язує лінійне порівняння виду ax=b(mod n)
    '''
    d=gcd(a, n) # рахую НСД
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
        


print(porivniia(33, 6, 72)) # Повертає [-26.0, -2.0, 22.0, 46.0], як було перевірено в ручну, то всі розв'язки правильні


        
        