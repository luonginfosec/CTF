unk_55F4CA40D080  = [0x42, 0xAA, 0xAA, 0xAA, 0xAA, 0xF1, 0xE2, 0x9B, 0x63, 0xE2, 0xA5, 0x1C, 0xAE, 0xA5, 0xAA, 0x62, 0x5C, 0x7A, 0x9E, 0xEE, 0xAE, 0xBD, 0x6A, 0x62, 0xA9, 0x82, 0x62, 0xE2, 0x27, 0xF9, 0xF9, 0x90, 0xAE, 0xA0, 0xDF, 0xBE, 0xE2, 0x55, 0x6B, 0xE2, 0x29, 0x53, 0x8A, 0xDF, 0x76, 0xE2, 0x27, 0xD9, 0xD2, 0x10, 0xB3, 0xAA, 0xAA, 0xAA, 0x41, 0xA6, 0xE2, 0x27, 0x19, 0x3B, 0xAA, 0xAA, 0xAA, 0x10, 0xB9, 0xAA, 0xAA, 0xAA, 0x12, 0xAB, 0xAA, 0xAA, 0xAA, 0x15, 0xAB, 0xAA, 0xAA, 0xAA, 0xA5, 0xAF, 0x69, 0x3A, 0x3A, 0x3A, 0x3A, 0x3A, 0x3A, 0x3A, 0x94, 0x91, 0x90, 0xB3, 0x32, 0x5F, 0x9D, 0x59, 0x3F, 0x6B, 0xB8, 0x4D, 0x77, 0x7A, 0xA4, 0x99, 0x66, 0xE1, 0xF2, 0xA3, 0xE4, 0x79, 0xA1, 0x39, 0xCE, 0xC8, 0x6C, 0xA4, 0x84, 0x14, 0x40, 0xE1, 0xAA, 0x0D, 0x17, 0x76, 0xA8, 0xD3, 0xC5, 0xDF, 0x8A, 0xCE, 0xCB, 0x8A, 0xD8, 0xC3, 0xC9, 0xCF, 0x8A, 0xCD, 0xC5, 0xCE, 0x8A, 0xC5, 0xD8, 0x8A, 0xDD, 0xC5, 0xDE, 0x95, 0xA0, 0xAA, 0xC7, 0xC5, 0xC4, 0xC1, 0x8A, 0xC6, 0xCB, 0xDF, 0xCD, 0xC2, 0xD9, 0x8A, 0xDE, 0xC5, 0xCE, 0xCB, 0xD3, 0xA0, 0xAA, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
n = 169
print(len(unk_55F4CA40D080))
byte_55F4CA40D138 = 0xaa
for i in range(0,n):
    unk_55F4CA40D080[i] ^= byte_55F4CA40D138
for i in range(0,len(unk_55F4CA40D080)):
    try:
        print(chr(unk_55F4CA40D080[i]),end="")
    except:
        print(end="")