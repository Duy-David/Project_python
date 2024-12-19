# n = int(input("Nhập số nguyên bất kỳ: "))
# sum = 0
# for i in range(n + 1):
#     sum += i
#     # tính tổng từ 0 -n
# print("Tổng từ 0 đến n: ", sum)

# # loop for ó bướng tăng tùy chỉnh

for i in range(0, 10, 2):
    print(i)

# duyệt các pahn62 tử trong list bằng vòng lập for
colors = ["red", "green", "yellow", "orange"]

for color in colors:

    print(color)

# duyệt các phần tử trong list theo vị trí bằng vòng lập for
for i in range(len(colors)):
    print(colors[i])


# In bảng cữu chhương
for j in range(1, 10):
    print("Bảng cữu chương: ", j)
    for i in range(1, 11):
        print("{0} * {1} = {2} ".format(j, i, j * i))
