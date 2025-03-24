enc = [
    198,
    232,
    816,
    200,
    1536,
    300,
    6144,
    984,
    51200,
    570,
    92160,
    1200,
    565248,
    756,
    1474560,
    800,
    6291456,
    1782,
    65536000
]
for i in range(1,20):
    if i & 1 != 0:
        enc[i - 1] = enc[i - 1] >> i
    else:
        enc[i - 1] = enc[i - 1] / i
print("".join(chr(int(c)) for c in enc))