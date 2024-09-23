v9 = "wodah"
text = ""
key3 = "kills"
text += (key3) + v9[::-1]
key1 = "ADSFK"
key1 += "SLCDN"[::-1]
key = key1
v3 = 0
v2 = 0
v5 = len(key)
key_list = list(key)
for i in range(v5):
    if 64 < ord(key_list[v3 % v5]) <= 90:
        key_list[i] = chr(ord(key_list[v3 % v5]) + 32)
    v3 += 1
key = ''.join(key_list)
ans = ""
for i in range(len(text)):
    j = 0
    while 1 > 0:
        tmp = ord(text[i]) - 97 + 26*j - 97 + ord(key[v3%v5]) + 39
        j = j + 1
        if tmp > 64 and tmp < 123:
            ans += chr(tmp)
            break
    v3 = v3 + 1
print("flag{"+ans+"}")
