FLAG_DECRYPT = ['p', 'v', 'k', 'q', '{', 'm', '1', '6', '4', '6', '7', '5', '2', '6', '2', '0', '3', '3', 'l', '4', 'm', '4', '9', 'l', 'n', 'p', '7', 'p', '9', 'm', 'n', 'k', '2', '8', 'k', '7', '5', '}']
print(len(FLAG_DECRYPT))
FLAG = [''] * 38
for i in range(len(FLAG_DECRYPT)):
    if((FLAG_DECRYPT[i] >= 'A' and FLAG_DECRYPT[i] <= 'Z') or (FLAG_DECRYPT[i] >= 'a' and FLAG_DECRYPT[i] <= 'z')):
        FLAG[i] = chr(ord(FLAG_DECRYPT[i]) + 16)
        if((FLAG[i] > 'Z' and FLAG[i] < 'a' ) or FLAG[i] >= 'z'):
            FLAG[i] = chr(ord(FLAG[i]) - 26)
    else:
        FLAG[i] = FLAG_DECRYPT[i] 
print("".join(c for c in FLAG))