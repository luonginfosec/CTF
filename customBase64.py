import base64

def custom_b64encode(data, custom_alphabet):
    standard_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    encoded = base64.b64encode(data).decode('utf-8')
    return encoded.translate(str.maketrans(standard_alphabet, custom_alphabet))

def custom_b64decode(encoded_data, custom_alphabet):
    standard_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    standard_data = encoded_data.translate(str.maketrans(custom_alphabet, standard_alphabet))
    return base64.b64decode(standard_data)

# Convert custom_alphabet to a list to make it mutable
custom_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
for i in range(10):
    v1 = custom_alphabet[i]
    custom_alphabet[i] = custom_alphabet[19 - i]
    custom_alphabet[19 - i] = v1
# Convert custom_alphabet back to a string
custom_alphabet = ''.join(custom_alphabet)
data = b"luongvd"
# Encode
encoded = custom_b64encode(data, custom_alphabet)
print("Encoded:", encoded)
# Decode
decoded = custom_b64decode("d2G0ZjLwHjS7DmOzZAY0X2lzX3CoZV9zdNOydO9vZl9yZXZlcnGlfD==", custom_alphabet)
print("Decoded:", decoded.decode('utf-8'))
