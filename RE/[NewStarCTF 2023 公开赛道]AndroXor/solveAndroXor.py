cArr = [14, ord('\r'), 17, 23, 2, ord('K'), ord('I'), ord('7'), ord(' '), 30, 20, ord('I'), ord('\n'), 2, ord('\f'), ord('>'), ord('('), ord('@'), 11, ord('\''), ord('K'), ord('Y'), 25, ord('A'), ord('\r')]
intArr = [14, 13, 17, 23, 2, 75, 73, 55, 32, 30, 20, 73, 10, 2, 12, 62, 40, 64, 11, 39, 75, 89, 25, 65, 13]
key = "happyx3"
flag = ""
for i in range(len(intArr)):
    flag += chr(intArr[i] ^ ord(key[i%len(key)]))
print(flag)