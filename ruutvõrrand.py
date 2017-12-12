#Thonny alguses liidab, siis lahutab, siis korrutab ja jagab ja astendab, lõpuks ta teeb suure tehte
print("Hello!")
myName = input("What is you name? ")
print("Hello, " + myName)
print("Let's solve a problem!")
import cmath
a = input("Please input a: ")
b = input("Please input b: ")
c = input("Please input c: ")
print("y = a*(x**) + b*x + c")
a = int(a)
b = int(b)
c = int(c)
d = pow(b,2) - 4*a*c
if d  < 0:
    print("No solutions")
else:
    x1 = round((-b + d**(1/2)) / 2*a)
    x2 = round((-b - d**(1/2)) / 2*a)
    print("y=(x-" + str(x1) + ")*(x-" + str(x2) + ")")