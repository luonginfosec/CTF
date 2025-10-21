# compute_first_half.py
const = [122,86,27,22,53,35,80,77,24,98,122,7,72,21,98,114]
key   = [66,51,122,33,86]
out = bytes([(c ^ key[i % len(key)]) & 0xff for i, c in enumerate(const)])
print(out)          # bytes representation
print(out.decode()) # decode as UTF-8 (should be printable)
