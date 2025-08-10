```Transformation```

```
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

[File enc](./enc)

## Phân tích đề

Câu lệnh mã hóa 

```Python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

Phân tích ```flag``` là chuỗi ban đầu.
```ord(flag[i])``` lấy mã ascii của kí tự thứ i 
```ord(flag[i]) << 8 + ord(flag[i + 1])``` dịch trái 8 byte cao.

Gộp 2 kí tự thành 1 kí tự, việc cần làm của chúng ta là bây giờ đã có enc thì phải tách được 1 kí tự thành 2 kí tự là sẽ khôi phục được lại flag ban đầu.

## Khai thác 

Chúng ta có chuỗi đã packed(kết quả của ''.join(...) gọi là packed). Mỗi kí tự c trong packed chứa hai kí tự gốc.

1. Đọc kí tự từ c từ packed 
2. Lấy giá trị số ascii
```val = ord(c)``` 
3. Tách byte cao(kí tự gốc thứ nhất)
```high = val >> 8``` dịch phải 8 bit chia cho 256 làm tròn xuống.
4. Tách 8 byte thấp(kí tự thứ hai)
```low = val & 0xFF```


Ví dụ cụ thể 

Ví dụ với hai kí tự gốc là 'A' và 'B':

- ord('A') = 65 = 0x41 = 01000001 (8 bit)
- ord('B') = 66 = 0x42 = 01000010 (8 bit)

Mã hóa:

```(ord('A') << 8 ) = 0x41 << 8 = 0x4100 =  01000001 00000000 (16 bit)```
```+ ord('B') => 0x4100 + 0x42 = 0x4142 = 01000001 01000010```

```chr(0x4142) đây là 1 kí tự Unicode```


Giải mã (lấy lại 'A' và 'B'):

```val = ord('䂂') = 0x4142```

```high = val >> 8 = 0x41 = 65 => chr(65) = 'A'```

```low = val & 0xFF = 0x42 = 66 => chr(66) = 'B'```

Tiến hành viết code giải mã bằng python như sau:

[Code solve](./solve.py)

```Python
def decode_enc_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()  
    decoded = ''.join([chr(ord(c) >> 8) + chr(ord(c) & 0xFF) for c in data])
    return decoded
flag = decode_enc_file("enc")
print(flag)
```

## Kết luận

Thu được flag ```picoCTF{16_bits_inst34d_of_8_04c0760d}```