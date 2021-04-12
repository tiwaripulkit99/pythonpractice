class Employee:
  num=35
class Program:
    num=67
class New(Employee,Program):
    pass
harry=New()
print(harry.num)
#inherit all properites of both the classes