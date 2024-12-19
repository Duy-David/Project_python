# Cộng str
s1 = "Xin chào"
s2 = "Phương Uyên"
print(s1 + " " + s2)
# chuổi nhiều dòng
linestr = """
line1 
line2
lìne3
"""
print(linestr)


# Kiểm tra chuổi con có thuộc chuổi khác
str1 = "Xin Chào"
str2 = "Xin"
str3 = "xám"

if str2 in str1:
    print("str2 là con của str1")
else:
    print("str2 là không con của str1")
if str3 in str1:
    print("str3 là con của str1")
else:
    print("str3 là không con của str1")

s = "uyen xinh quá"
# Viết hoa chu đầu chuổi
print(str.capitalize(s))
# Viết hoa toàn  bộ chuổi
print(s.upper())
# Viết thưởng toàn  bộ chuổi
print(s.lower())

#tìm kiếm ,thay thế ,đếm số lượng chuổi con
s="Lập trình Python, bạn nên học Python"
print(s.find("Python"))
print(s.count("Python"))
print(s.replace("Python","PYTHON"))


# cắt chuổi thành list
list="Lập trình Python, bạn nên học Python"
print(list.split(" "))