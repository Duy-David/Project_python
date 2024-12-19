# Xây dựng một từ điểm có các chức năng
# 1.Thêm một từ mới
# 2. tra cưu từvựng
# 3.Cập nhật ý nghĩa cho một từ vựng
# 4 cho phép người dùng xóa đi mtộ từ vựng trong từ điển
# 5. cho phép người dùng xóa toàn bộ từ vựng
# 6. cho phép người dùng in toàn bộ từ vựng
# 7 cho phép người dùng in toàn bộ từ vựng và ý nghĩa của nó
# 8.Kết thúc chương trình

# Khai báo từ điển
tuDien = {}
while True:
    print("Vui lòng lữa chọn chưc năng:")
    print(
        """ 1.Thêm một từ mới\n 2.Tra cứu từ vựng \n 3.Cập nhật ý nghĩa cho một từ vựng\n 4.Cho phép người dùng xóa đi một từ vựng trong từ điển\n 5.Cho phép người dùng xóa toàn bộ từ vựng\n 6.Cho phép người dùng in toàn bộ từ vựng\n 7.Cho phép người dùng in toàn bộ từ vựng và ý nghĩa của nó\n 8.Kết thúc chương trình\n"""
    )
    luaChon = int(input("Nhập vào lựa chon của bạn: "))

    if luaChon == 1:
        tuVung = str(input("nhập vào từ vựng:"))
        yNghia = str(input("nhập vào ý nghĩa:"))
        tuDien[tuVung] = yNghia
        print("Đã thêm dự liệu")
    elif luaChon == 2:
        tuVung = input("nhập vào từ vựng:")
        print("Ý Nghĩa: ", tuDien[tuVung])
        print("Tra cưu từ vựng thành công")
    elif luaChon == 3:
        tuVung = str(input("nhập vào từ vựng:"))
        yNghia = str(input("nhập vào ý nghĩa:"))
        tuDien[tuVung] = yNghia
        print("Đã cấp nhật dữ liệu")
    elif luaChon == 4:
        tuVung = input("nhập vào từ vựng cần xóa:")
        tuDien.pop(tuVung)
        print("Đã xóa dữ liệu")
    elif luaChon == 5:
        tuDien.clear()
        print("đã xóa toàn bộ dữ liệu")
    elif luaChon == 6:
        print("Danh sách các từ vụng có trong từ điển")
        for x in tuDien.keys():
            print(x)
    elif luaChon == 7:
        for x, y in tuDien.items():
            print(x, " : ", y)
    elif luaChon == 8:
        break
    else:
        print("Nhập lựa chọn không đúng")
