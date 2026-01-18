#!/usr/bin/env python3
import re, sys

wat_path = sys.argv[1] if len(sys.argv) > 1 else "program_gc.wat"
lines = open(wat_path, "r", encoding="utf-8", errors="ignore").read().splitlines()

# type 9: func_id -> ascii_code
type9 = {}
for i, line in enumerate(lines):
    m = re.search(r"\(func\s+\(;(\d+);\).*\(type\s+9\)", line)
    if not m:
        continue
    fid = int(m.group(1))
    for j in range(i, min(i + 6, len(lines))):
        cm = re.search(r"i32\.const\s+(\d+)", lines[j])
        if cm:
            type9[fid] = int(cm.group(1))
            break

# type 19: func_id -> position
type19_pos = {}
for i, line in enumerate(lines):
    m = re.search(r"\(func\s+\(;(\d+);\).*\(type\s+19\)", line)
    if not m:
        continue
    fid = int(m.group(1))
    pos = None
    for j in range(i, min(i + 12, len(lines))):
        if "i32.eqz" in lines[j]:
            pos = 0
            break
        cm = re.search(r"i32\.const\s+(\d+)", lines[j])
        if cm and (j + 1) < len(lines) and "i32.eq" in lines[j + 1]:
            pos = int(cm.group(1))
            break
    if pos is not None:
        type19_pos[fid] = pos

# processor globals
pos_to_char = {}

print("=== Dump struct.new 27 lines + mapping ===")
for idx, line in enumerate(lines):
    if "(ref 27)" not in line or "struct.new 27" not in line:
        continue

    funcs = [int(x) for x in re.findall(r"ref\.func\s+(\d+)", line)]
    print(f"\n[Line {idx}] {line}")
    print(f"  ref.func list = {funcs}")

    if len(funcs) < 4:
        print("  (skip: funcs < 4)")
        continue

    t9 = funcs[1]
    t19 = funcs[3]

    ascii_code = type9.get(t9)
    pos = type19_pos.get(t19)

    if ascii_code is None or pos is None:
        print(f"  (skip: t9={t9} ascii={ascii_code}, t19={t19} pos={pos})")
        continue

    ch = chr(ascii_code)
    print(f"  -> pos={pos:2d}, ch='{ch}', t9_func={t9} (ascii={ascii_code}), t19_func={t19}")

    # nếu trùng pos thì in cảnh báo
    if pos in pos_to_char and pos_to_char[pos] != ch:
        print(f"  !!! WARNING: pos {pos} already '{pos_to_char[pos]}', new '{ch}'")

    pos_to_char[pos] = ch

print("\n=== Result ===")
password = "".join(pos_to_char.get(i, "?") for i in range(30))
print("password =", password)
print("flag     =", f"uoftctf{{{password}}}")
