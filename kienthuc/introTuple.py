# tuple giốn với list tuy nhiên list thay dổi giá trị con được còn tuple thì không
gioiTinh = ("nam", "nữ")
traiCay = ("táo", "mít", "Cam", "táo", "mận")
print(traiCay)
print(gioiTinh[0])
# traiCay[0]="mận"
for x in traiCay:
    print(x)

# nối phần tử
y = (1, 2, 3) + (4, 5, 6)

print(y)
print(y * 2)

print("bom" in traiCay)
print(max(traiCay))

print(min(traiCay))
print(traiCay.count("táo"))
print(traiCay.count("bom"))
print(sum(y))
print(sorted(traiCay))
