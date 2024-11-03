v8 = "5B134977135E7D13"
v8 = bytes.fromhex(v8)
v8 = list(v8)
v7 = [0x10 , 0x20 , 0x30]
for i in range(len(v8)):
    v8[i] = (v8[i]) ^ v7[i % 3]
print("".join(chr(x) for x in v8))