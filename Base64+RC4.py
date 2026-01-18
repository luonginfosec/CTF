import base64
from Crypto.Cipher import ARC4
custom_b64 = ""
standard_b64 = ""
decode_map = str.maketrans(custom_b64, standard_b64)
def decode_custom_base64(s: str) -> bytes:
    s_translated = s.translate(decode_map)
    s_padded = s_translated + '=' * (-len(s_translated) % 4)
    return base64.b64decode(s_padded)
custom_encoded = ""
key = b""
decoded_bytes = decode_custom_base64(custom_encoded)
cipher = ARC4.new(key)
decrypted = cipher.decrypt(decoded_bytes)
print(decrypted.decode('utf-8', errors='replace'))
