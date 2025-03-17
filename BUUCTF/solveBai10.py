text = "killshadow"
key = "adsfkndcls"
v3 = 10

for i in range(10):  
    for j in range(65, 123):  
        if ('A' <= chr(j) <= 'Z') or ('a' <= chr(j) <= 'z'):  
            if ((j - 39 - ord(key[v3 % 10]) + 97) % 26 + 97) == ord(text[i]):  
                v3 += 1
                print(chr(j), end="")
                break
