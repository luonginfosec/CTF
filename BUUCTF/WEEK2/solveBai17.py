code = [
    '\x1f',
    '\x12',
    '\x1d',
    '(',
    '0',
    '4',
    '\x01',
    '\x06',
    '\x14',
    '4',
    ',',
    '\x1b',
    'U',
    '?',
    'o',
    '6',
    '*',
    ':',
    '\x01',
    'D',
    ';',
    '%',
    '\x13']
for i in range(len(code)):
    code[i] = ord(code[i])
for i in range(len(code) - 2, - 1, - 1):
    code[i] ^= code[i + 1]
for i in range(len(code)):
    code[i] = (code[i] - i) % 128
print("".join(chr(c) for c in code))