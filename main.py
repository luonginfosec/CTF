import time
from pywinauto import Application

# Kết nối với ứng dụng bgb64.exe (đảm bảo nó đang chạy)
try:
    app = Application().connect(title_re=".*bgb64.*")  # Tìm cửa sổ có tên chứa "bgb64"
    window = app.top_window()  # Lấy cửa sổ chính của ứng dụng

    # Đưa cửa sổ lên trước
    window.set_focus()

    # Nhấn phím "s" liên tục
    while True:
        window.send_keystrokes("s")

except Exception as e:
    print(f"Lỗi: {e}. Đảm bảo bgb64.exe đang chạy!")
