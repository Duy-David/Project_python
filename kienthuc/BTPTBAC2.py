# ta có pt bậc 2 :ax2+bx+C=0
import math

# nhập các hệ số
a = float(input(" hệ số a: "))
b = float(input(" hệ số b: "))
c = float(input(" hệ số c: "))
print("ta có Pt bậc 2 : {0}x^2 + {1}x + {2} = 0".format(a,b,c))
if a != 0:
    delta = b**2 - 4 * a * c

    if delta < 0:
        print(" Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x =", -b / (2 * a))
    else:
        print(
            "Phương trình có 2 nghiệm x1= {0} , x2={1}".format(
                (-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)
            )
        )

else:
    print("không phải PT bậc 2")
# tính delta
