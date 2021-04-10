#exception handling
a=int(input("enter the no1:"))
b=int(input("enter the no2:"))
try:
    print(a+b)
except Exception as e:
    print(e)
print("this is very important")
