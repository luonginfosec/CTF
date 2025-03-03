enc = "6!!sbn*ass%84z@84c(8o_^4#_#8b0)5m_&j}y$vvw!h"
def sub_1418(input_str: str) -> int:
    input_list = list(input_str) 
    length = len(input_list)
    half_length = length // 2
    v3 = 0

    while v3 < half_length:
        v2 = input_list[v3]
        input_list[v3] = input_list[length - 1 - v3]
        input_list[length - 1 - v3] = v2
        v3 += 1

    return half_length, "".join(input_list)
def reverse_sub_12CB(modified_str: str) -> str:
    original = []  
    for i, ch in enumerate(modified_str):
        if i % 4 != 1: 
            original.append(ch)
    return "".join(original)
def reverse_sub_1199(encoded_str: str, mapping: str) -> str:
    dest = list(encoded_str)
    for i, ch in enumerate(encoded_str):
        if ch in mapping:
            j = mapping.index(ch)
            dest[i] = mapping[(j - 7) % len(mapping)]  
    return "".join(dest)
enc = sub_1418(enc)[1]
enc = reverse_sub_12CB(enc)
enc = reverse_sub_1199(enc,"0123456789abcdefghijklmnopqrstuvwxyz_{}")
print(enc)