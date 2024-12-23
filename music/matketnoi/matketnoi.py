import time
import sys
import pygame

pygame.mixer.init()

# Phát nhạc nền
pygame.mixer.music.load(r"C:\Users\Admin\Desktop\IT\PYTHON\music\matketnoi\dist\MatKetNoi-DuongDomic-16783113.mp3")
pygame.mixer.music.play(0, start=90.0)  # Lặp vô hạn cho đến khi chương trình kết thúc


def show_each_letter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Xuống dòng sau khi hiển thị xong


def fade_in_text(text, delay=0.05):
    for i in range(1, len(text) + 1):
        sys.stdout.write("\r" + text[:i])  # Hiển thị dần từng ký tự
        sys.stdout.flush()
        time.sleep(delay)


# Nội dung
print("\n")
lines = [
    ("show", "Cuộc gọi nhỡ cho em hàng đêm\n", 0.04, 0.5),
    ("fade", "\t\t\t Đến tận 200 lần", 0.05, 0.7),
    ("show", "Dòng ký ức trong em về anh\n", 0.05, 0.7),
    ("fade", "\t\t\t Bây giờ đang phai dần", 0.05, 0.7),
    ("show", "Quay gót rời đi\n", 0.05, 0.7),
    ("fade", "\t\t Không để lại gì", 0.05, 1.2),
    ("show", "Bay vút qua tầm tay\n", 0.04, 0.7),
    ("fade", "\t\t\t Sao còn vương vấn để làm gì...", 0.03, 0.9),
    ("show", "Bọn mình kết thúc thật rồi\n", 0.03, 0.7),
    ("fade", "\t Hết sức thật rồi", 0.03, 0.3),
    ("fade", "\t Phải không em ơi", 0.01, 1.4),
    ("show", "Chuyện tình có khúc phải lòng\n", 0.03, 0.5),
    ("fade", "\t Có lúc phải rời", 0.03, 0.5),
    ("fade", "\t Vậy đến lúc rồi", 0.03, 1.3),
    ("show", "Và có lẽ giờ này\n", 0.03, 1.2),
    ("show", "Em đã ngủ say\n", 0.03, 1.2),
    ("show", "Còn anh thì vẫn mang\n", 0.02, 1.7),
    ("fade", "\t\t Nỗi nhớ em trong đêm thật dài", 0.02, 2.7),
    ("fade", "\t\t Thêm lý do cho anh tồn tại", 0.03, 2.5),
    ("fade", "\t\t Để lại chạm vào bờ môi ấy dịu dàng", 0.02, 2.5),
    ("show", "Lời thì thầm ngọt ngào bên tai\n", 0.06, 2.0),
    ("fade", "\t Ta mất nhau thật rồi em ơi", 0.05, 2.5),
    ("fade", "\t Tan vỡ hai cực đành chia đôi", 0.02, 3.0),
    ("fade", "\t Anh sẽ luôn ghi nhớ em", 0.06, 0.08),
    ("fade", "\t Trong từng tế bào ", 0.05, 0.3),
    ("show", "Vậy mà dừng lại như thế sao...\n", 0.04, 3.8),
    ("fade", "\t\t Trong anh hay là trong em đã đổi thay bao nhiêu suy nghĩ", 0.02, 3),
    ("fade", "\t\t Yêu thương nay còn đâu", 0.02, 1.5),
    ("fade", "\t\t Anh còn yêu, nghe hơi vô lý", 0.06, 0.08),
    ("fade", "\t\t Ta mất kết nối thật rồi", 0.06, 0.08),
]

# Thực thi
for mode, text, delay, sleep_time in lines:
    if mode == "show":
        show_each_letter(text, delay=delay)
    elif mode == "fade":
        fade_in_text(text, delay=delay)
        print()  # Xuống dòng cho rõ ràng
    time.sleep(sleep_time)

# Hiển thị dòng cuối đặc biệt với 3 dấu "..."
line25 = "Đã mất kết nối thật rồi em ơi!..."
if line25.endswith("..."):
    main_text = line25[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.09)
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print()

# Dừng nhạc khi kết thúc
pygame.mixer.music.stop()
