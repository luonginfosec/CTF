#!/usr/bin/env python3
import re
from pathlib import Path

WAT_PATH = "program_gc.wat"  # đổi nếu file bạn nằm chỗ khác

def wat_string_to_bytes(lit: str) -> bytes:
    """Convert WAT string literal content into raw bytes (handles \hh hex escapes)."""
    out = bytearray()
    i = 0
    while i < len(lit):
        c = lit[i]
        if c != "\\":
            out.append(ord(c))
            i += 1
            continue

        # hex escape: \hh
        if i + 2 < len(lit) and re.fullmatch(r"[0-9a-fA-F]{2}", lit[i+1:i+3]):
            out.append(int(lit[i+1:i+3], 16))
            i += 3
            continue

        # common escapes
        if i + 1 < len(lit):
            nxt = lit[i + 1]
            if nxt == "n": out.append(10); i += 2; continue
            if nxt == "r": out.append(13); i += 2; continue
            if nxt == "t": out.append(9);  i += 2; continue
            if nxt == '"': out.append(ord('"')); i += 2; continue
            if nxt == "\\": out.append(ord("\\")); i += 2; continue
            # fallback: keep char after backslash
            out.append(ord(nxt))
            i += 2
            continue

        out.append(ord("\\"))
        i += 1

    return bytes(out)

def load_pool_utf16le(wat_path: str) -> str:
    wat = Path(wat_path).read_text("utf-8", errors="replace")

    # lấy đúng data segment 0
    m = re.search(r"\(data\s+\(;0;\)\s+\"([\s\S]*?)\"\)\s*\n\s*\(data\s+\(;1;\)", wat)
    if not m:
        raise RuntimeError("Không tìm thấy (data (;0;)) hoặc pattern khác với script này.")

    data0_bytes = wat_string_to_bytes(m.group(1))
    # decode UTF-16LE
    pool = data0_bytes.decode("utf-16le", errors="replace")
    return pool

def main():
    pool = load_pool_utf16le(WAT_PATH)
    print(f"Loaded string pool. Total chars: {len(pool)}")
    print("Nhập: <offset> <length>  (offset tính theo BYTE, length tính theo số ký tự)")
    print("Gõ q để thoát.\n")

    while True:
        s = input("offset length > ").strip()
        if not s:
            continue
        if s.lower() in ("q", "quit", "exit"):
            break

        try:
            off_str, len_str = s.split()
            off = int(off_str, 0)   # hỗ trợ 0x...
            ln  = int(len_str, 0)
        except Exception:
            print("Sai format. Ví dụ: 6394 15\n")
            continue

        if off % 2 != 0:
            print("⚠️ Offset lẻ. Pool là UTF-16LE nên offset thường phải chẵn (byte). Mình vẫn sẽ cắt bằng off//2.")

        start = off // 2
        end = start + ln
        if start < 0 or end > len(pool):
            print(f"Out of range: start={start}, end={end}, pool_len={len(pool)}\n")
            continue

        sub = pool[start:end]
        print("Substring (repr):", repr(sub))
        print("Substring (plain):", sub)
        print("Actual length (Python chars):", len(sub))
        print()

if __name__ == "__main__":
    main()
