flag = ""
f1 = "GXY{do_not_"
flag += f1
v4 = '\x7Ffo`guci'[::-1]
v4 = [ord(x) for x in v4]
for i in range(0,8):
    if(i % 2 == 1):
        v4[i] = v4[i] - 2
    elif(i % 2 == 0):
        v4[i] = v4[i] - 1
f2 = "".join(chr(x) for x in v4)
flag += f2
print(flag)