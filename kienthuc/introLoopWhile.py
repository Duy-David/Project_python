# yêu cầu người dùng nhập vào một số n>0, nếu nhập sai thì nhập lại
n = -1
while n <= 0:
    n = int(input("nhập vào n:"))

i = 0
tong = 0
while i <= n:
    tong += i
    i += 1
print("tổng: ", tong)

# lopp while-else

j = 0
while j <= 5:
    print(j, "- Bên trong vòng lập")
    j += 1
    if j >= 3:
        break
else:
    print(j, "- Bên ngoài vòng lập")
