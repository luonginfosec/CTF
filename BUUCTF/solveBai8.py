import base64

str_enc = "e3nifIH9b_C@n@dH"
str_enc = list(str_enc)

for i in range(len(str_enc)):
    str_enc[i] = chr(ord(str_enc[i]) - i)

decoded_str = "".join(str_enc)
decoded_bytes = base64.b64decode(decoded_str)
print(decoded_bytes.decode(errors="ignore"))  
