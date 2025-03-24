import string

v12 = "Qsw3sj_lz4_Ujw@l"
v12 = [ord(x) for x in v12]  

listStr = string.ascii_letters  
listStr = [ord(c) for c in listStr]

print(len(v12))

for i in range(len(v12)):
    oke = 0
    for j in listStr:
        if j >= 97:
            if(v12[i] == (j - 79)%26 + 97):
                oke = 1
                print(chr(j),end="")
                break
        elif j >= 65:
            if(v12[i] == (j - 51)%26 + 65):
                oke = 1
                print(chr(j),end="")
                break
    if oke == 0:
        print(chr(v12[i]),end="")