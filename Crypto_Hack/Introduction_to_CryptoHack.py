import base64
from Crypto.Util.number import *
def func1():
    flag = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    print(''.join(chr(i) for i in flag))
    flag1 = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
    print(bytes.fromhex(flag1)) #convert hex to string
    flag2 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    print(base64.b64encode(bytes.fromhex(flag2)))
    flag3 = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    print(long_to_bytes(flag3).decode())
    flag4 = "label"
    decode_flag4 = ""
    for x in flag4:
        decode_flag4 += chr(ord(x) ^ 13)
    print("crypto{" + decode_flag4 + "}")
    key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
    key2 = key1 ^ 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
    key3  = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1 ^ key2
    flag5 = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf ^ key1 ^ key2 ^ key3
    print(long_to_bytes(flag5))
    flag6 = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    hex_arr_flag6 = [x for x in bytes.fromhex(flag6)]
    for i in range(256):
        possible_flag_arr = [x ^ i for x in hex_arr_flag6]
        possible_flag = "".join(chr(x) for x in possible_flag_arr)
        if(possible_flag.startswith("crypto")):
            print(possible_flag)
            break
mess = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
key_xor = "myXORkey"
mess = [c for c in bytes.fromhex(mess)]
key_xor = [ord(c) for c in key_xor]
flag_done = ""
for i in range(len(mess)):
    flag_done += chr(mess[i] ^ key_xor[i%len(key_xor)])
print(flag_done)