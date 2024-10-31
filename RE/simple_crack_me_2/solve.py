encode = [0xF8, 0xE0, 0xE6, 0x9E, 0x7F, 0x32, 0x68, 0x31, 0x05, 0xDC, 0xA1, 0xAA, 0xAA, 0x09, 0xB3, 0xD8, 0x41, 0xF0, 0x36, 0x8C, 0xCE, 0xC7, 0xAC, 0x66, 0x91, 0x4C, 0x32, 0xFF, 0x05, 0xE0, 0xD9, 0x91, 0x00]
unk_402072 = [0x11, 0x33, 0x55, 0x77, 0x99, 0xBB, 0xDD, 0x00]
unk_402068 = [0xDE, 0xAD, 0xBE, 0xEF, 0x00, 0xEF, 0xBE, 0xAD, 0xDE, 0x00, 0x11, 0x33, 0x55, 0x77, 0x99, 0xBB, 0xDD, 0x00]
unk_40206D = [0xEF, 0xBE, 0xAD, 0xDE, 0x00]
def sub_4011B6(a1):
    v2 = 0
    while a1[v2] != 0:
        v2 += 1
    return v2
def sub_4011EF(a1, a2):
    v4 = sub_4011B6(a2)
    for i in range(len(a1)):
        a1[i] ^= a2[i % v4]
    return a1
def sub_401263(a1, a2):
    for i in range(len(a1)):
        a1[i] += a2
    return a1
def sub_4012B0(a1, a2):
    for i in range(len(a1)):
        a1[i] -= a2
    return a1
def decode_sub_4011EF(a1, a2):
    v4 = sub_4011B6(a2)
    for i in range(len(a1)):
        a1[i] ^= a2[i % v4]
    return a1
def decode_sub_401263(a1, a2):
    for i in range(len(a1)):
        a1[i] -= a2
    return a1
def decode_sub_4012B0(a1, a2):
    for i in range(len(a1)):
        a1[i] += a2
    return a1
decode_sub_4011EF(encode, unk_402072)
decode_sub_401263(encode, 243)
decode_sub_4012B0(encode, 77)
decode_sub_4011EF(encode, unk_40206D)
decode_sub_4012B0(encode, 90)
decode_sub_401263(encode, 31)
decode_sub_4011EF(encode, unk_402068)
for i in range(len(encode)):
    if encode[i] < 0:
        encode[i] += 256
print("".join(chr(x) for x in encode))