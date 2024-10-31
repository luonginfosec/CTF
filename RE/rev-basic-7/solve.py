byte_140003000 = [ 
   82, 223, 179,  96, 241, 139,  28, 181,  87, 209, 
  159,  56,  75,  41, 217,  38, 127, 201, 163, 233, 
   83,  24,  79, 184, 106, 203, 135,  88,  91,  57, 
   30
]
def ror(value, shift, bits=8):
  value = value >> shift | value << (bits-shift)
  return value % 256
def calculate_a1(byte_140003000):
    a1 = []
    for i in range(len(byte_140003000)):
        a1_value = ror(byte_140003000[i] ^ i, i & 7)
        a1.append(a1_value)
    return a1
a1 = calculate_a1(byte_140003000)
for x in a1:
  print(chr(x),end="")