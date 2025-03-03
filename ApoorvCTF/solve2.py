def rol(value, bits, width=8):
    """Rotate left (ROL) operation."""
    mask = (1 << width) - 1  # Giới hạn trong 8-bit
    return ((value << bits) & mask) | ((value & mask) >> (width - bits))

def decrypt(enc):
    plaintext = []
    for v1 in range(len(enc)):
        # Giải phương trình: enc[v1] = ROR1(((~(v1 + input[v1]) ^ 0x44) + 23), 3) - v1
        rotated_back = (enc[v1] + v1) & 0xFF  # Giải ROR1 trước
        original_value = rol(rotated_back, 3)  # Đảo ngược ROR1 bằng ROL

        # Đảo ngược ((~(v1 + input[v1]) ^ 0x44) + 23)
        original_value = (original_value - 23) & 0xFF  # Trừ 23
        original_value ^= 0x44  # XOR với 0x44
        inverted_value = ~original_value & 0xFF  # Đảo bit

        # Giải phương trình v1 + input[v1] = inverted_value
        input_byte = (inverted_value - v1) & 0xFF
        plaintext.append(input_byte)

    return bytes(plaintext)

# Giải mã chuỗi enc
decoded_text = decrypt([0x3E, 0x3B, 0x3A, 0x19, 0x98, 0xF5, 0x37, 0xF3, 
                        0x95, 0xC1, 0x12, 0xE7, 0xDD, 0xD0, 0x0E, 0x33, 
                        0xCC, 0x4B, 0x58, 0x09, 0x4E, 0xD3, 0x0B, 0x93, 
                        0x64, 0x62, 0xC6, 0x0E, 0x2E, 0xBE, 0xEA, 0x4B, 
                        0x00, 0xA7, 0xBD, 0xDC, 0x02])

print(decoded_text.decode(errors='ignore'))# Giải mã ra chuỗi có thể đọc được
