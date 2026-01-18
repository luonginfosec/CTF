import builtins
import contextlib
import io

# Proxy đại diện cho "một phần" của chuỗi input: có thể là 1 ký tự hoặc 1 đoạn slice
class SliceProxy:
    def __init__(self, hook_string, indices):
        self.hook = hook_string          # tham chiếu về HookString
        self.indices = tuple(indices)    # tuple các index trong input mà proxy đang đại diện

    def __getitem__(self, key):
        """
        Cho phép slice/index tiếp trên proxy.
        Ví dụ: s[10:20][2:5] vẫn hoạt động và ra proxy mới.
        """
        if isinstance(key, slice):
            return SliceProxy(self.hook, self.indices[key])
        if isinstance(key, int):
            return SliceProxy(self.hook, (self.indices[key],))
        raise TypeError("Only slice/int supported")

    def __eq__(self, other):
        """
        Khi baby.py làm: if s[a:b] == "expected":
        => gọi __eq__ tại đây.
        Ta log ra constraint rồi trả True để chương trình chạy tiếp.
        """
        print(self.indices, other)
        self.hook.constraints.append((self.indices, other))
        return True


# "Chuỗi giả" thay cho input thật
class HookString:
    def __init__(self, length):
        self.length = length
        self.constraints = []  # list các (indices_tuple, expected)

    def __len__(self):
        # để pass check len(s) == 74
        return self.length

    def __getitem__(self, key):
        """
        Khi baby.py truy cập s[i] hoặc s[a:b] => trả SliceProxy tương ứng.
        """
        if isinstance(key, slice):
            # chuẩn hóa slice theo length (xử lý None, âm, vượt biên)
            start, stop, step = key.indices(self.length)
            return SliceProxy(self, range(start, stop, step))

        if isinstance(key, int):
            # hỗ trợ index âm
            if key < 0:
                key += self.length
            return SliceProxy(self, (key,))

        raise TypeError("Only slice/int supported")


def run_with_hook(path_to_baby="baby.py", entry_func="gog0sQu1D", length=74):
    # buffer hứng stdout
    buf = io.StringIO()

    # namespace để exec baby.py
    ns = {}

    # object input giả
    fake_s = HookString(length)

    # exec baby.py => các hàm/biến nằm trong ns
    exec(open(path_to_baby, "r", encoding="utf-8").read(), ns, ns)

    # fake input: in prompt vào buffer rồi trả fake_s
    def fake_input(prompt=""):
        print(prompt, end="", file=buf)
        return fake_s

    # redirect stdout vào buf + patch builtins.input
    with contextlib.redirect_stdout(buf):
        original_input = builtins.input
        builtins.input = fake_input
        try:
            ns[entry_func]()   # chạy hàm chính
        finally:
            builtins.input = original_input

    # in ra toàn bộ output + trả constraint để post-process nếu cần
    print(buf.getvalue())
    return fake_s.constraints


if __name__ == "__main__":
    constraints = run_with_hook("baby.py", "gog0sQu1D", 74)
    # constraints là list (indices_tuple, expected_string)
    # bạn có thể dùng nó để ráp flag.
