import math

a=int(input("Enter a value: "))
b=float(input("Enter b value: "))
dif=abs(a-b)

if(dif < .001):
    print("Close")
else:
    print("Not close")    