# break
for i in range(10):
    if i > 5:
        break
    print(i)

n = 100
while n > 0:
    print(n)
    n = n // 2
    if n < 50:
        break


# continue

for i in range(0,10):
    if i %2==1:
        continue
    print(i )