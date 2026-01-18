import re
from pathlib import Path

WAT_PATH = "program_gc.wat"

def wat_string_to_bytes(lit: str) -> bytes:
    """
    WAT string literal uses escapes like \\00, \\ef, \\\", \\\\ etc.
    This converts the inside of "..." into raw bytes.
    """
    out = bytearray()
    i = 0
    while i < len(lit):
        c = lit[i]
        if c != "\\":
            out.append(ord(c))
            i += 1
            continue

        if i + 1 >= len(lit):
            out.append(ord("\\"))
            break

        nxt = lit[i + 1]

        # hex escape: \hh
        if i + 2 < len(lit) and re.fullmatch(r"[0-9a-fA-F]{2}", lit[i+1:i+3]):
            out.append(int(lit[i+1:i+3], 16))
            i += 3
            continue

        # common escapes
        if nxt == "n": out.append(10); i += 2; continue
        if nxt == "r": out.append(13); i += 2; continue
        if nxt == "t": out.append(9);  i += 2; continue
        if nxt == '"': out.append(ord('"')); i += 2; continue
        if nxt == "\\": out.append(ord("\\")); i += 2; continue

        # fallback: keep the char after backslash
        out.append(ord(nxt))
        i += 2

    return bytes(out)

wat = Path(WAT_PATH).read_text("utf-8", errors="replace")

# 1) lấy data segment 0 (string pool)
m = re.search(r"\(data \(;0;\)\s+\"([\s\S]*?)\"\)\s*\n\s*\(data \(;1;\)", wat)
if not m:
    raise SystemExit("Không tìm thấy data segment 0")

data0_bytes = wat_string_to_bytes(m.group(1))

# 2) decode UTF-16LE thành một chuỗi lớn (pool)
pool = data0_bytes.decode("utf-16le", errors="replace")

# 3) tìm mọi chỗ gọi call 88 theo pattern: i32.const X / offset / len / call 88
call88 = re.compile(
    r"i32\.const\s+\d+\s+"
    r"i32\.const\s+(?P<off>\d+)\s+"
    r"i32\.const\s+(?P<len>\d+)\s+"
    r"call\s+88"
)

seen = set()
for mm in call88.finditer(wat):
    off = int(mm.group("off"))
    ln  = int(mm.group("len"))
    start = off // 2              # vì offset tính theo BYTE, UTF-16LE = 2 byte/ký tự
    s = pool[start:start+ln]
    if (off, ln, s) in seen:
        continue
    seen.add((off, ln, s))
    print(f"{off:5d} {ln:3d}  {s!r}")
