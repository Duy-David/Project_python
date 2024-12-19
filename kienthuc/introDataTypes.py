x = 1
print(type(x))


x = 1.111
print(type(x))


x = 1 + 2j
print(type(x))


x = "abc"
print(type(x))


x = True
print(type(x))


x = None
print(type(x))


# ép kiểu dữ liệu
# kiễu cdữ iệu nào lớn để ép kiểu

a = 5
b = 2.0
c = a / b
print("a:{0}".format(type(a)))
print("b:{0}".format(type(b)))
print("c:{0}".format(type(c)))


# ép kiểu bằng hàm
n = 100
m = "200"

print(n + int(m))
print(m + str(n))
