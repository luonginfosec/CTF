flag = ""
f1 = "GXY{do_not_"
flag += f1
s = '\x7Ffo`guci'[::-1]
s = [ord(x) for x in s]
v5 = 0
for i in range(0,8):
    if(i % 2 == 1):
        s[i] = s[i] - 2
    elif(i % 2 == 0):
        s[i] = s[i] - 1
f2 = s
f2 = "".join(chr(x) for x in f2)
flag += f2
print(flag)