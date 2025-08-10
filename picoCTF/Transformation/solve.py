def decode_enc_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()  
    decoded = ''.join([chr(ord(c) >> 8) + chr(ord(c) & 0xFF) for c in data])
    return decoded
flag = decode_enc_file("enc")
print(flag)
