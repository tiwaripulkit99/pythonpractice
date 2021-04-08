x=int(input("enter the first number"))
y=int(input("enter the second number"))
z=int(input("enter the third number"))
if x>y and x>z:
    print("%d is greater"%x)
elif y>x and y>z:
    print("%d is greater" %y)
elif z>x and z>y:
    print("%d is greater" %z)
else:
    print("enter a valid number")
