monHoc = {"toán", "văn", "anh"}
print(monHoc)
for x in monHoc:
    print(x)
# thêm phần tử
monHoc.add("lịch sữ")
print(monHoc)

hocThem = {"hóa", "lý"}
monHoc.update(hocThem)
print(monHoc)
# thêm list vào trong set
hocPhuDao = ["võ", "đàn", "võ"]
monHoc.update(hocPhuDao)
print(monHoc)
# xóa phần tữ
monHoc.remove("võ")
# nếu có th2i xóa còn không có thì bỏ qua không bị lỗi
monHoc.discard("võ")
#xóa phần tử đầu tiên
monHoc.pop()
# xóa tất cả các phần tữ
monHoc.clear()