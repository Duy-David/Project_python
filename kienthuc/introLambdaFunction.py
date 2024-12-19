# khai báo Lambda Function
kiemtraSoChan = lambda a: (a % 2 == 0)
print(kiemtraSoChan(5))
print(kiemtraSoChan(4))

tinhTong = lambda a, b: a + b

print(tinhTong(5, 10))


def hamMu(n):
    return lambda x: x**n


hammu2 = hamMu(2)
hammu3 = hamMu(3)
hammu4 = hamMu(4)

print(hammu2(5))
print(hammu3(3))
print(hammu4(2))
