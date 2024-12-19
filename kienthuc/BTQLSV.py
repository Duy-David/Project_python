import sqlite3

# Tao ket61 noi61 voi17 cssdl
connect = sqlite3.connect("C:/Users/Admin/Desktop/IT/PYTHON/db/student.db")
# print(connect)
# Tạo thông tin lớp
cursor = connect.cursor()

# Xóa table nếu đã tồn tại
cursor.execute("DROP TABLE IF EXiSTS lop_hoc")
# tạo  mới table

sql = """
   CREATE TABLE lop_hoc (
    ma_lop TEXT (50) NOT NULL PRIMARY KEY,
    ten_lop TEXT (250) NULL DEFAULT NULL
);
"""
cursor.execute(sql)

# Insert dữ liệu
data = [
    ("L001", "Toán 10A"),
    ("L002", "Lý 10B"),
    ("L003", "Hóa 10C"),
    ("L004", "Anh 11A"),
    ("L005", "Sinh 11B"),
]

cursor.executemany("INSERT INTO lop_hoc (ma_lop, ten_lop) VALUES (?, ?)", data)

connect.commit()
connect.close()


# Tao ket61 noi61 voi17 cssdl

# KẾt nối với CSDL
connect = sqlite3.connect("C:/Users/Admin/Desktop/IT/PYTHON/db/student.db")
# print(connect)
# Tạo thông tin lớp
cursor = connect.cursor()

# Xóa bảng nếu đã tồn tại
cursor.execute("DROP TABLE IF EXISTS sinh_vien")

# Tạo bảng mới
sql = """
CREATE TABLE sinh_vien (
    masv TEXT (50) NOT NULL PRIMARY KEY,
    hotensv TEXT (250) NULL DEFAULT NULL,
    ngaysinh DATE NULL DEFAULT NULL,
    ma_lop TEXT (255) NOT NULL,
    FOREIGN KEY(ma_lop) REFERENCES lop_hoc(ma_lop)
);
"""
cursor.execute(sql)

# Thêm 5 dữ liệu mẫu
data = [
    ("SV001", "Nguyen Van A", "2005-01-15", "L001"),
    ("SV002", "Tran Thi B", "2005-02-20", "L002"),
    ("SV003", "Le Van C", "2005-03-10", "L003"),
    ("SV004", "Pham Thi D", "2004-11-25", "L004"),
    ("SV005", "Hoang Van E", "2004-12-05", "L005"),
]

cursor.executemany(
    "INSERT INTO sinh_vien (masv, hotensv, ngaysinh, ma_lop) VALUES (?, ?, ?, ?)", data
)

# Lưu thay đổi và đóng kết nối
connect.commit()
connect.close()

print("Tạo bảng và thêm dữ liệu thành công!")
