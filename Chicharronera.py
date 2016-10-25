import math
a=int(input("Dame a: "))
b=int(input("Dame b: "))
c=int(input("Dame c: "))
x1=((-1*b)+(math.sqrt((b**2)-(4*a*c))))/2*a
x2=((-1*b)-(math.sqrt((b**2)-(4*a*c))))/2*a
print("Las raices de ",a,", ",b,", ",c," es: ")
print("x1= ",x1,"\nx2= ",x2)
