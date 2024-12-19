n = -1
while n <= 0:
    n = int(input("nhập vào n:"))
# Chuyển từ nhị phân sang thập phân
ketQua = ""
while n > 0:
    ketQua = str(n % 2)+ketQua
    n = n // 2
print(ketQua)
