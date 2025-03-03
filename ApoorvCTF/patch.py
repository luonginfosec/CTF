with open("evil-rice-cooker", 'rb') as f:
    code = f.read()
    
offset = 0x3080
length = 0xa9

code = bytearray(code)
for i in range(offset, offset + length):
    code[i] ^= 0xaa
    
with open("patched", 'wb') as f:
    f.write(code)
print(code)