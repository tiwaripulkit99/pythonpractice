limit=int(input("enter any number"))


for j in range(1,limit+1):
    num = j
    fact=1
    for i in range(num, 0, -1):
        fact = fact * i
    print("factorial of %d"%num,"is=",fact)

