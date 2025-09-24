from PIL import Image

rows, cols = 5, 6
tile_w, tile_h = 82, 98
orig_w, orig_h = 490, 490
padded_w, padded_h = 492, 490

file_order = [
    "piece_03.png", "piece_14.png", "piece_06.png", "piece_04.png", "piece_00.png", "piece_22.png",
    "piece_16.png", "piece_01.png", "piece_09.png", "piece_18.png", "piece_21.png", "piece_26.png",
    "piece_20.png", "piece_11.png", "piece_10.png", "piece_07.png", "piece_13.png", "piece_28.png",
    "piece_25.png", "piece_29.png", "piece_17.png", "piece_12.png", "piece_27.png", "piece_23.png",
    "piece_05.png", "piece_24.png", "piece_19.png", "piece_08.png", "piece_02.png", "piece_15.png"
]

canvas = Image.new("RGB", (padded_w, padded_h), "white")

for idx, fname in enumerate(file_order):
    r = idx // cols
    c = idx % cols
    img = Image.open(fname)
    x, y = c * tile_w, r * tile_h
    canvas.paste(img, (x, y))

final_qr = canvas.crop((0, 0, orig_w, orig_h))
final_qr.save("qr_reconstructed.png")

print("✅ Đã ghép QR thành công theo thứ tự file, lưu ở qr_reconstructed.png")