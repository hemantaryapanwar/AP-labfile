import math
wish=int(input("Enter 1-logarithmic function \n 2-absolute function \n 3-power function \n 4-trignometric function \n 5-inverse trignometric function"))
if(wish==1):
    b=float(input("Enter the base b"))
    a=float(input("Enter the number to be taken log to the base {0}".format(b)))
    c=math.log(a,b)
    print(f"{a} log to the base {b} is {c}")
elif(wish==2):
    a=float(input("Enter the number"))
    c=math.fabs(a)
    print(f"absolute {a} is {c}")
elif(wish==3):
    x=float(input("Enter x in x^y"))
    y=float(input("Enter the power of {0}".format(x)))
    c=math.pow(x,y)
    print(f"{x} to the power {y} is {c}")
elif(wish==4):
    a=float(input("Enter the angle in degree"))
    b=math.sin(a*math.pi/180)
    c=math.cos(a*math.pi/180)
    d=math.tan(a*math.pi/180)
    print(f"sin({a}) = {b}")
    print(f"cos({a}) = {c}")
    print(f"tan({a}) = {d}")
