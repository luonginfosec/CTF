byte_40F0E0 = [
  0x67, 0x79, 0x7B, 0x7F, 0x75, 0x2B, 0x3C, 0x52, 0x53, 0x79, 
  0x57, 0x5E, 0x5D, 0x42, 0x7B, 0x2D, 0x2A, 0x66, 0x42, 0x7E, 
  0x4C, 0x57, 0x79, 0x41, 0x6B, 0x7E, 0x65, 0x3C, 0x5C, 0x45, 
  0x6F, 0x62, 0x4D
]
byte_414040 = byte_40F0E0
dword_40F040 = [
  0x09 , 0x0A , 0x0F, 
   0x17 , 0x07 , 
  0x18 , 0x0C , 0x06, 
   0x01 , 0x10 , 
  0x03 , 0x11 , 0x20, 
   0x1D , 0x0B , 
  0x1E , 0x1B , 0x16, 
   0x04 , 0x0D , 
  0x13 , 0x14 , 0x15, 
   0x02 , 0x19 , 
  0x05 , 0x1F , 0x08, 
   0x12 , 0x1A , 
  0x1C , 0x0E, 0x00
]
input = [0] * 34
for i in range(len(byte_40F0E0)):
    byte_40F0E0[i] ^= dword_40F040[i] % 0xFF
    input[int(dword_40F040[i])] = byte_40F0E0[i]
print("".join(chr(x) for x in input))