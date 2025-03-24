from Crypto.PublicKey import RSA
from Crypto.Util.number import *


f = open('pub.key','r')
key = RSA.importKey(f.read())
n = key.n
e = key.e

print(f'{n=}\n{e=}')


p = 285960468890451637935629440372639283459
q = 304008741604601924494328155975272418463
n = p*q
phi = (p-1)*(q-1)
e = 65537
d = inverse(e, phi)

with open('flag.enc', 'rb') as f:
    s = f.read()
    c = bytes_to_long(s)

print(long_to_bytes(pow(c, d, n)))