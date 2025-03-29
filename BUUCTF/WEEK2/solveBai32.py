from Crypto.Util.number import inverse, long_to_bytes

# Cho trước
p = 282164587459512124844245113950593348271
q = 366669102002966856876605669837014229419
N = p * q
e = 65537
c = int("ad939ff59f6e70bcbfad406f2494993757eee98b91bc244184a377520d06fc35", 16)

# Tính φ(N)
phi = (p - 1) * (q - 1)

# Tính d (private key)
d = inverse(e, phi)

# Giải mã flag
m = pow(c, d, N)
flag = long_to_bytes(m)

print(flag.decode())
