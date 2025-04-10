def gcd(a, b):
    '''
    Функцію просто взяла з першої лабороторної по ТЧА, бо можна
    '''
    if a == 0 and b == 0:
        return 0
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)
    