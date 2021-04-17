"""current=int(input("enter current age or year of birth:"))
if current>=1800 and current<2022:
    age_in_2021=2021-current
    remaining=100-age_in_2021
    print("you will be of 100 at ",remaining+2021)

elif current>2021:
    print("you are not born yet")
else:
    print("you will be of 100 at after  ", 100 - current - 1, "years")"""
"""import random

def galat(number):
    wrong= random.randint(1,9)
    table=[i*number for i in range(1,11)]
    table[wrong]=table[wrong]+random.randint(0,9)
    return table
def iscorrect(table,number):
    for i in range(1,11):
      if table[i-1]!=i*number:
        return i-1
if __name__ == '__main__':
    number = int(input("enter num"))
    mytable=galat(number)
    print(mytable)
    print(iscorrect(mytable,number))
    wrongindex=iscorrect(mytable,number)
    print(f"the index value of wrong is :{wrongindex}")"""

"""try:
    print(10/0)
except Exception as e1:
    print(e1)
else:
    print("sab thik hai")

finally:
    print("done successfully",e)


"""
#practice sets
"""def readfile(filename):
    try:
      with open(filename,'r') as f:
        print(f.read())
    except FileNotFoundError:
        print(f"{filename} file not found")
readfile("1.txt")
readfile("2.txt")
readfile("3.txt")
"""
"""list=[10,20,30,40,50,60,70,80]
for index,item in enumerate(list):
    if index==3 or index==7 or index==5:
       print(index,item)"""


while(True):
 number = int(input('enter the no:'))
 s = [i * number for i in range(1, 11)]
 print(s)
 with open("1.txt",'a')as f:
    f.write(str(s))
    f.write("\n")
    if number==5:
        exit()