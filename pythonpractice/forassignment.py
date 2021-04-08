sum1=0
limit=int(input("enter limit:"))
print("Number\tsquare")
for i in range(1,limit+1):

    s=i**2
    print(i,s)
    sum1=sum1+s
print("sum=",sum1)