"""import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
"""
"""s = 0
for d in range(0, 5, 0.1):
  s += d
  print(s)"""
"""def f(x = 100, y = 100):
   return(x+y, x-y)
x, y = f(y = 200, x = 100)
print(x, y)"""

"""class Ex:
   def __init__(self):
      self.name="pulkit"
   def fun1(self,name2):
      self.name2=name2
      print(self.name2)
ob1=Ex()
print(ob1.name)
ob1.fun1("john")
"""

"""name

age

gender

department

exp in years

salary

basic pay scale

hra"""
"""class Employee:
   def __init__(self,name,age,gender,department,exp,salary,basicpayscale,hra):
      self.name=name
      self.age=age
      self.gender=gender
      self.department=department
      self.exp=exp
      self.salary=salary
      self.basicpayscale=basicpayscale
      self.hra=hra


class EmployeeChild(Employee):
   pass
ob1=EmployeeChild("pulkit",21,"Male","IT","5year","1crpernnum","100000","500000")
print(ob1.name)
print(ob1.age)
print(ob1.gender)
print(ob1.department)
print(ob1.exp)
print(ob1.salary)
print(ob1.basicpayscale)
print(ob1.hra)


"""


"""class Employee_Deatails:
   def __init__(self, name, age, gender):
      self.name = name
      self.age = age
      self.gender = gender


class Employee_Com(Employee_Deatails):

   def __init__(self, name, age, gender, department, exp, salary, basic_pay_scale, hra):
      self.name = name
      self.age = age
      self.gender = gender
      self.department = department
      self.exp = exp
      self.salary = salary
      self.basic_pay_scale = basic_pay_scale
      self.hra = hra

   def show(self):
      print('Employee Name:', self.name)
      print('Employee Age:', self.age)
      print('Employee Gender:', self.gender)
      print('Employee department:', self.department)
      print('Employee exp in year:', self.exp)
      print('Employee salary:', self.salary)
      print('Employee basic_pay_scale:', self.basic_pay_scale)
      print('Employee hra:', self.hra)


emp = Employee_Com('somesh', 25, 'male', 'cloud', 2, 25000, 15000, 1500)
emp.show()"""



class Base(object):
   pass
class derived(Base):
   pass
print(issubclass(derived,Base))
print(issubclass(base,derived))

