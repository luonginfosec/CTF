
with open('', 'r') as file:
    binary_string = file.read().strip()

binary_segments = binary_string.split()

hex_segments = [hex(int(segment, 2))[2:].zfill(2).upper() for segment in binary_segments]

hex_string = " ".join(hex_segments)

with open('', 'w') as file:
    file.write(hex_string)

