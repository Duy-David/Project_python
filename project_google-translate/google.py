import googletrans
from googletrans import Translator


print(googletrans.LANGUAGES)
# Khởi tạo đối tượng Translator
trans = Translator()
print(trans)
# Dịch văn bản
translated = trans.translate(text="xin chao  bé ",dest="en", src="vi")


# In kết quả dịch
print(f"Original text: {translated.origin}")
print(f"Translated text: {translated.text}")
