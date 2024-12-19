# khai báo một class
class SimpleClass:
    # class attribute
    i = 3

    # init (hàm tạo)
    def __init__(self):
        self.j = 8

    # methods
    def printMe(self):
        print(self.j)


objectA = SimpleClass()
objectB = SimpleClass()
# objectA.printMe()
# print(objectB.i)
# thay đổi giá trị thuộc tính
objectA.i = 100
objectB.j = 500
# print(objectA.i)
# print(objectB.i)
# objectB.printMe()
# objectA.printMe()


class SimpleClass2:
    # tạo ra contructor
    def __init__(self):
        self.name = "Duy"

    # methods: muốn sữ dụng thì phải có một đối tượng cụ thể thì mới sữ dũng được
    def hello(self):
        print("hello " + self.name)

    # Static method: Không cần dối tượng để gọi
    @staticmethod
    def hi(name):
        print("hi " + name)


objectC = SimpleClass2()
objectD = SimpleClass2()

objectC.hello()
SimpleClass2.hi("Uyên")
# bên trogn phương thức có thể truyền vào tham số


# BT Xây dựng class ngyà ,gồm những thuoc5 tính :ngày,tháng , năm
# xay dựng các phương thức: cho biết đó là ngày thứ máy trong năm,staticmethod cho biết tháng đó có bao nhiêu ngày


class Ngay:
    # contructor
    def __init__(self, giaTriNgay, giaTriThang, giaTriNam):
        self.ngay = giaTriNgay
        self.thang = giaTriThang
        self.nam = giaTriNam

    # Xác định số ngày của tháng
    @staticmethod
    def soNgayCuaThang(thang, nam):
        if thang in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif thang in [4, 6, 9, 11]:
            return 30
        elif thang == 2:
            if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
                return 29
            else:
                return 28

    def ngayTrongNam(self):
        giaTriNgayTrongNam = 0
        for x in range(1, self.thang):
            giaTriNgayTrongNam += self.soNgayCuaThang(x, self.nam)
        giaTriNgayTrongNam+=self.ngay

        return giaTriNgayTrongNam
    
ngayA=Ngay(13,3,2025)
print(ngayA.ngayTrongNam())
# print(Ngay.soNgayCuaThang())