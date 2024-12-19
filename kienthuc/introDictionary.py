# khai báo  Dictionary
sinhVien = {"hoVaTen": "Phuong Duy", "maLop": "003", "diemTB": 8.5}
# lấy giá trị từ key
print(sinhVien["hoVaTen"])
print(sinhVien.get("maLop"))

# thay đổi value của key
sinhVien["maLop"] = "004"
print(sinhVien)
sinhVien.update({"maLop": "005", "diemTB": 9.5})
print(sinhVien)

# thêm key
sinhVien["gioiTinh"] = "nam"
print(sinhVien)
sinhVien.update({"namHoc": "2005"})
print(sinhVien)

# Xóa bỏ key
sinhVien.pop("gioiTinh")
print(sinhVien)
del sinhVien["namHoc"]
print(sinhVien)
# Xóa bỏ key cuối cùng
sinhVien.popitem()
print(sinhVien)
# Xóa hản  Dictionary
del sinhVien
sinhVien = {"hoVaTen": "Phuong Duy", "maLop": "003", "diemTB": 8.5}
# xóa các key trong dictionary
sinhVien.clear()
print(sinhVien)
sinhVien = {"hoVaTen": "Phuong Duy", "maLop": "003", "diemTB": 8.5}
# duyệt các giá trị có trong  dictionary
for x in sinhVien.values():
    print(x)
# duyệt các key có trong  dictionary
for x in sinhVien.keys():
    print(x)
# duyệt các cập có trong  dictionary
for x, y in sinhVien.items():
    print(x, y)

