import base64
strEnc = "VlxRV2t0II8kX2WPJ15fZ49nWFEnj3V8do8hYy9t"
strEnc = base64.b64decode(strEnc)
strEnc = list(strEnc)
print(strEnc)
flag = ""
for i in range(0,30):
    strEnc[i] = (strEnc[i] - 16) ^ 0x20
    flag += chr(strEnc[i])
print(flag)