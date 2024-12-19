# định nghĩa function
def xinChao():
    print("helloword")


xinChao()
# tham  số Và  biến


def xinChao(hoVaTen):
    print("helloword", hoVaTen)


xinChao("Mss.Uyên")


# Khi không xác định được dối số thì sữ dụng vào *
def thoiKhoaBieu(*monHoc):
    print("Môn một: " + monHoc[0])
    print("Môn hai: " + monHoc[1])


thoiKhoaBieu("toán", "lý", "hóa", "văn")


def sum(*giaTri):
    sum = 0
    for i in giaTri:
        sum += i
    print(sum)


sum(4, 12, 12, 23, 45)

# Truyền nhiều đối số xác định thông qua tên, sữ dụng **


def xinChao1(**name):
    print("xin Chao", name["ho"], name["ten"])


xinChao1(ho="Phuong", ten="Uyên")


# sữ dụng từ khóa retrun
def tinhTich(*giaTri):
    tich = 1
    for x in giaTri:
        tich *= x
    return tich


print(tinhTich(1, 4, 6))

# Tìm ước số chung LN của 2 si61 TN a,b
# xây dựng hàm:gcd(a,b)=>{trả về giNN}


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


print(gcd(55, 100))


# Nhập vào một dãy số từ bàn phím, sau đo tính tỏng

listNumber = []
n = -1
while True:
    try:
        n = int(input("Nhập vào số lượng phần tử: "))
    except:
        print("Vui lòng nhập n>=1")
    if n >= 1:
        break


def nhap(n, listNumber):
    for i in range(n):
        listNumber.append(int(input("Nhập vào giá trị thứ :" + str(i) + ": ")))


def tinhTong(listNumber):
    tong = 0
    for i in listNumber:
        tong += i
    return tong

nhap(n,listNumber)
print(tinhTong(listNumber))
