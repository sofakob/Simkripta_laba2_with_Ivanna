
def algoritm_evklida_with_input():
    b=int(input("Введіть число до якого треба знайти обернене: "))
    a=int(input("Введіть модуль за яким треба знайти обернене: "))
    if b>a:
        b%=a
    q=0
    u=1; v=0; u1=0; v1=1
    while a>b:
        c=a
        while c>b:
            c=c-b
            q+=1
        a=b; b=c
        u2=u-u1*q
        v2=v-v1*q
        u=u1; v=v1; u1=u2; v1=v2; q=0
    print(f"Обернене число дорівнює: {v1}")

def algoritm_evklida_with_a_b(b:int, a:int):
    if b>a:
        b%=a
    q=0
    u=1; v=0; u1=0; v1=1
    while a>b:
        c=a
        while c>b:
            c=c-b
            q+=1
        a=b; b=c
        u2=u-u1*q
        v2=v-v1*q
        u=u1; v=v1; u1=u2; v1=v2; q=0
    return v1
    
print(algoritm_evklida_with_a_b(5, 12))