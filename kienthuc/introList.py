# tạo list
emptylist = []
# tạo ra một đối tượng list
emptylist2 = list()

print(emptylist)
print(emptylist2)

colors = ["red", "green", "yellow", "orange"]
print(colors)
studentList = ["An", "Bình", "Ngân", "Uyên"]

# print(studentList[x:y]) là lấy ra list    [x:y)
print(studentList[3])
print(studentList[:])
print(studentList[2:4])

# them phân tử vào  cuối list
studentList.append("Duyên")
studentList[len(studentList):] =["Phương"]
# them phân tử vào  bất kỳ ở đâu list

studentList.insert(2,"Thanh")
studentList.insert(3,"Thanh")
studentList.insert(5,"Thanh")
print(studentList)
# số lượng phần  tử
print(len(studentList))

#đếm số lượng phàn tữ

print(studentList.count("Thanh"))
print(studentList.count("An"))

# Xóa phần tử ra khỏi list theo giá trị
studentList.remove("Ngân")
# studentList.remove("Ngân")
print(studentList)


# Kiểm tra phần tử có bên trong list in

if "An" in studentList:
    studentList.remove("An")
    print(studentList)

if "An" in studentList:
    studentList.remove("An")
    print(studentList)




#  Xóa phần tử ra khỏi list theo vị trí
studentList.pop(1)
print(studentList)


# chuyển dổi ngược các phần tử  list

studentList.reverse()
print(studentList)

# xắp sếp tăng dần các phần tử
studentList.sort()
print(studentList)

# xắp sếp giảm dần các phần tử
studentList.sort(reverse=True)
print(studentList)

# xóa sạch ddử liệu bên trong list
number = [1,4,5,6,7,3]
number.clear()
print(number)

