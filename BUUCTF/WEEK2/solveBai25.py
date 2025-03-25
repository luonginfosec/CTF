import hashlib
from itertools import product

target_hash = "6E32D0943418C2C33385BC35A1470250DD8923A9".lower()
suffix = "@DBApp"

def sha1_hash(value: str) -> str:
    return hashlib.sha1(value.encode()).hexdigest()

def brute_force():
    for num in product("0123456789", repeat=6):
        candidate = "".join(num) + suffix
        if sha1_hash(candidate) == target_hash:
            print("Found match:", candidate)
            return candidate
    print("No match found")


brute_force()

def xor_bytes(input_str, key_bytes):
    input_bytes = input_str.encode()  
    result = [input_bytes[i] ^ key_bytes[i] for i in range(len(input_bytes))]
    return bytes(result).decode(errors='ignore') 
input_str = "{\\rtf1"
key_bytes = [0x05, 0x7D, 0x41, 0x15, 0x26, 0x01]

output = xor_bytes(input_str, key_bytes)
print(output)  