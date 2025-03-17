x = list("dd2940c04462b4dd7c450528835cca15")

x[2] = chr((ord(x[2]) + ord(x[3])) - 50)
x[4] = chr((ord(x[2]) + ord(x[5])) - 48)
x[30] = chr((ord(x[31]) + ord(x[9])) - 48)
x[14] = chr((ord(x[27]) + ord(x[28])) - 97)

for i in range(16):
    x[31 - i], x[i] = x[i], x[31 - i]

x = "".join(x)
print(x)
