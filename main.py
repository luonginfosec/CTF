import struct

# Dữ liệu so sánh trong chương trình
encoded_bytes = bytes([
    0xB6, 0x9E, 0xAD, 0xC5, 0x92, 0xFA, 0xDF, 0xD5, 
    0xA1, 0xA8, 0xDC, 0xC7, 0xCE, 0xA4, 0x8B, 0xE1, 
    0x8A, 0xA2, 0xDC, 0xE1, 0x89, 0xFA, 0x9D, 0xD2, 
    0x9A, 0xB7
])

key = 0xBEEFCAFE
decoded_bytes = bytearray()

for i in range(0, len(encoded_bytes), 4):
    chunk = encoded_bytes[i:i+4]
    chunk = chunk.ljust(4, b'\x00')  # Đệm nếu không đủ 4 bytes
    num = struct.unpack('<I', chunk)[0]  # Chuyển thành số nguyên 4 byte (Little Endian)
    decoded = num ^ key  # XOR với key
    decoded_bytes.extend(struct.pack('<I', decoded))  # Đưa về dạng bytes

flag = decoded_bytes.rstrip(b'\x00').decode(errors='ignore')  # Xóa null bytes và giải mã
print(f"Flag: {flag}")

# import random
# byte_4120 = [
#     55, 136, 17, 148, 205, 207, 18, 221, 213, 239, 122, 93, 184, 45, 171, 87,
#     140, 143, 19, 215, 153, 27, 151, 159, 14, 73, 35, 83, 84, 108, 90, 204,
#     220, 201, 26, 200, 234, 85, 174, 216, 223, 245, 120, 228, 33, 163, 100, 218,
#     127, 154, 164, 86, 150, 249, 29, 237, 91, 24, 11, 160, 241, 236, 230, 44,
#     116, 15, 70, 31, 135, 98, 16, 141, 106, 210, 8, 177, 211, 167, 182, 124,
#     99, 183, 133, 32, 40, 74, 111, 192, 39, 41, 81, 5, 212, 217, 2, 152,
#     118, 138, 175, 113, 191, 68, 28, 248, 104, 252, 22, 185, 63, 21, 253, 129,
#     112, 103, 227, 115, 47, 109, 53, 64, 77, 169, 142, 38, 67, 50, 131, 242,
#     254, 179, 61, 197, 10, 42, 117, 238, 132, 196, 95, 181, 187, 158, 46, 65,
#     60, 23, 25, 190, 57, 145, 247, 172, 6, 231, 13, 246, 161, 34, 69, 168,
#     76, 30, 134, 48, 88, 155, 149, 92, 170, 229, 198, 36, 97, 208, 56, 139,
#     4, 79, 123, 75, 94, 0, 199, 80, 66, 156, 176, 186, 137, 195, 226, 7,
#     125, 20, 82, 225, 144, 146, 126, 214, 1, 128, 240, 107, 89, 78, 173, 251,
#     165, 206, 51, 119, 203, 180, 3, 52, 71, 209, 178, 222, 147, 202, 121, 59,
#     62, 58, 193, 224, 243, 72, 162, 49, 9, 188, 235, 12, 189, 105, 54, 110,
#     166, 101, 43, 250, 233, 255, 244, 157, 130, 37, 96, 194, 114, 102, 219, 232
# ]

# # Simulated `unk_40C0` pointer (indices into byte_4120)
# unk_40C0_indices = [random.randint(0, 255) for _ in range(24)]  # Replace with actual indices

# # Extract flag characters
# flag = "".join(chr(byte_4120[i]) for i in unk_40C0_indices)
# print(f"Flag: {flag}")
