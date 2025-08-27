import zlib

v25 = [
    0xB969BE79, 0xBE047A60, 0xDD0216B9, 0xBE047A60, 0x3DD7FFA7,
    0xBE047A60, 0x4DBD0B28, 0x15D54739, 0x4AD0CF31, 0x83DCEFB7,
    0x7808A3D2, 0x8D076785, -186917087, -1637089325, 701932520,
    1466425173, -227710402, -2068763730, 1790921346, -69523947,
    701932520, 1037565863, -206169288, 1812594589, 30677878,
    -186917087, 701932520, -2082672713, 2013832146, 701932520,
    -1107002784, -1855256857, 1842515611, 701932520, 1466425173,
    1842515611, 1801730948, 1842515611, 0x6C09FF9D, 0x84B12BAE,
    0x6DD28E9B, 0xFCB6E20C
]

v25 = [(x + (1 << 32)) & 0xFFFFFFFF for x in v25]

decoded = ""

for crc in v25:
    found = None
    for c in range(32, 127):  # ASCII printable
        b = bytes([c])
        calc = zlib.crc32(b) & 0xFFFFFFFF
        if calc == crc:
            found = chr(c)
            break
    decoded += found if found else '?'

print(decoded)
