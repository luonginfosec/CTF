from binascii import unhexlify
from Crypto.Cipher import AES

key = unhexlify("C47ADB30CABD55D9F782A619DA2FF9654822FEDE61065F76934F29560F4FE4EA")
blob = unhexlify("C0684CBE81D689762CA24055FFB13BA901956C4EF34F1965CDDCC11299372CBC76AE485361985AA98B8A5111371A574E9C878B03DCB53B12C47F469A0AA63327")
iv, ct = blob[:16], blob[16:]
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ct)
pad = pt[-1]
if 1 <= pad <= 16 and all(b==pad for b in pt[-pad:]):
    pt = pt[:-pad]
print(pt.decode())
