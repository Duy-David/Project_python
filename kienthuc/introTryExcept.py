# Thực hiện bắt lôi
"""
try:
# d9oạn code dự đoán có lỗi

except:
#hành động khi lỗi xẫy ra

else:
#thực thi đọan này nếu không có lỗi

finally:
#cho phép bạn thực thi mã,bất kễ các khối try có bị lỗi hay không
"""
try:
    a = int(input("Nhập số nguyên vào a: "))

    print(str(a) + " + 5 = " + str(a + 5))
except:
    print("Nhập dữ liệu không chính xác")
else:
    print("Không có lỗi")
finally:
    print("Kết thúc chương trình")
# try:
#     a = int(input("Nhập số nguyên vào a: "))

#     print(str(a) + " + 5 = " + str(a + 5))
# except Exception as e:
#     print(e)
