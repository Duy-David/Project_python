# import thư viện
import sqlite3

# kết nối với database
path = "C:/Users/Admin/Desktop/IT/PYTHON/db/csdl.db"
connection = sqlite3.connect(path)

# print(connection)

# Ngắt kết nối với database
# connection.close()
# tạo đối tượng cursor
cursor = connection.cursor()

# tạo câu lệnh SQL
# sql = "SELECT * FROM sinhvien"
# sql = "SELECT * FROM sinhvien where sinhvien.diemtb>=7"
# sql="insert into sinhvien(masv,hovaten,diemtb) values('04','Tran van A',9)"
# sql="update sinhvien set diemtb=diemtb+3" 
sql="delete from sinhvien where masv ='05'" 

cursor.execute(sql)
connection.commit()

# result = cursor.fetchall()

# print(result)
cursor.close()


