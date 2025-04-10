def gcd(a, b):
    if a == 0 and b == 0:
        return 0
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)
    