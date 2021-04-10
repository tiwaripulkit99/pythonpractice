#exception handling
a=(input("enter the no1:"))
b=(input("enter the no2:"))
try:
    print("the sum is ",int(a)+int(b))
except Exception as e:
    print(e)
print("this is very important")
