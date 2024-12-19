# x = int(input("nhập vào số nguyên: "))
# # Toán tư 3 ngôi
# kq = "chẳn" if (x % 2 == 0) else "lẽ"
# print(kq)

# if x > 0:
#     print(x, "là số dương")
# else:
#     print(x, "là số âm")

# câu lệnh if elif else
a = int(input("nhập vào số điểm: "))

if a>=9:
    print("Xếp loại xuất sắc")
elif 9>a>=8:
    print("Xếp loại giõi")
elif 8>a>=6:
    print("Xếp loại khá")
elif 6>a>=5:
    print("Xếp loại tb")
else:
    print("tạch cmmr")
print("kết thúc chương trình")