from binascii import unhexlify, hexlify
key = unhexlify("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
encrypted1 = unhexlify("939FCF9C9B9998C99DC8C9989ECFCB9A")
encrypted2 = unhexlify("9F9D9D9DCB989A9B999A98CF9DCFCFCF")
def decrypt(data, key):
  decrypted = bytearray()
  for i in range(len(data)):
    decrypted.append(data[i] ^ key[i])
  return decrypted
decrypted1 = decrypt(encrypted1, key)
decrypted2 = decrypt(encrypted2, key)
part1 = decrypted1[::-1].decode()
part2 = decrypted2[::-1].decode()
flag = part1 + part2
print(f"Flag: {flag}")

