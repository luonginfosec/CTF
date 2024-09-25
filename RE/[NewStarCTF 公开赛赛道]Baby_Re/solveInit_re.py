final = [102, 109, 99, 100, 127, 86]
byte_4066 = [
  105, 106, 109, 125, 98
]
byte_406B = [
  98, 98, 106, 81, 125, 101, 127, 77, 113, 113, 
  115
]
byte_4076 = [
  121, 101, 125, 70, 119, 122, 117, 115
]
byte_407E = [
  33, 98
]
byte_4066[0] = 54
byte_406B[0] = 58
byte_4076[0] = 38
byte_407E[0] = 63
data_done = final + byte_4066 + byte_406B + byte_4076 + byte_407E
i = 0
for i in range(len(data_done)):
    v3 = i
    if v3 >= len(data_done):
        break
    data_done[i] ^= i
    i = i + 1
print("".join(chr(x) for x in data_done))