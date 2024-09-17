def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
print(gcd(66528,52920))
p = 26513
q = 32321
def extended_gcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)
gcd1 , u , v = extended_gcd(p,q)
print(u,v)