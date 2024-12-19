import pyttsx3
from PyPDF2 import PdfReader

# Mở file PDF
book = open("software_engineering_tutorial.pdf", "rb")
pdfReader = PdfReader(book)

# Lấy số lượng trang
pages = len(pdfReader.pages)
print(f"Number of pages: {pages}")


# Khởi tạo pyttsx3
bot = pyttsx3.init()

# Lấy danh sách giọng nói
voices = bot.getProperty("voices")

# Chọn giọng nữ (hoặc bất kỳ giọng nào bạn muốn)
bot.setProperty("voice", voices[1].id)  # voices[1] thường là giọng nữ trên Windows

# Đọc trang cụ thể (ví dụ: trang số 2 - index là 1)
for num in range(8, pages):
    page = pdfReader.pages[num]
    text = page.extract_text()
    bot.say(text)

    # Chạy pyttsx3 để đọc nội dung
    bot.runAndWait()
