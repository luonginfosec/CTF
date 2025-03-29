v12 = "Iodl>Qnb(ocy\x7Fy.i\x7Fd`3w}wek9{iy=~yL@EC"
v12 = list(v12)
for i in range(len(v12)):
    print(chr(ord(v12[i]) ^ i),end="")
print(end="\n")
byte_6CC0A0_byte_6CC0A3 = [
  0x40, 0x35, 0x20, 0x56, 0x5D, 0x18, 0x22, 0x45, 0x17, 0x2F, 
  0x24, 0x6E, 0x62, 0x3C, 0x27, 0x54, 0x48, 0x6C, 0x24, 0x6E, 
  0x72, 0x3C, 0x32, 0x45, 0x5B
]
key = [0] * 4
know = "flag"
know = list(know)
for i in range(0,4):
    key[i] = ord(know[i]) ^ byte_6CC0A0_byte_6CC0A3[i]
for i in range(0,len(byte_6CC0A0_byte_6CC0A3)):
    print(chr(byte_6CC0A0_byte_6CC0A3[i] ^ key[i % 4]),end="")