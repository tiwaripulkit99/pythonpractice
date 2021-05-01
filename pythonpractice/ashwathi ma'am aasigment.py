# this show we can use nayname instead of self:
"""class test:
   def __init__(myobject,a):
      myobject.country=a

   def myfunc(abc):
      print(abc.country)
ob1=test("india")
ob1.myfunc()"""
# classwork:
"""
class Employee_Deatails:

   def __init__(self):
      self.name = 'somesh'
      self.age = 24
      self.gender = 'male'

   def show(self):
      print('Employee name:', self.name)
      print('Employee age:', self.age)
      print('Employee gender:', self.gender)


class Employee_Com(Employee_Deatails):

   def __init__(self):
      self.department = 'Cloud'
      self.exp = 2

   def show1(self):
      print('Employee department:', self.department)
      print('Employee exp in year:', self.exp)


class Empl_Sal(Employee_Com):

   def __init__(self):
      Employee_Deatails.__init__(self)
      Employee_Com.__init__(self)
      self.salary = 25000
      self.basic_pay_scale = 15000
      self.hra = 1500

   def show2(self):
      Employee_Deatails.show(self)
      Employee_Com.show1(self)
      print('Employee salary:', self.salary)
      print('Employee basic_pay_scale:', self.basic_pay_scale)
      print('Employee hra:', self.hra)


emp = Empl_Sal()
emp.show2()
"""

"""
class Base(object):
    pass


class derived(Base):
    pass


print(issubclass(derived, Base))
print(issubclass(Base, derived))
d = derived()
b = Base()
print(isinstance(b, derived))
print(isinstance(d, Base))
"""
#Aswathi, 10:36 AM
#display student details,language total marks,subject total mark

"""class studentdetails:
    def name(self):
        self.st1='pulkit'
        self.st2='john'
        self.st3='shubham'
        self.st4='salman'
        print(self.st1,self.st2,self.st3,self.st4)
        self.st1age="21"
        self.st2age="23"
        self.st3age="24"
        self.st4age="22"
        print("age of st1=",self.st1,"age of st1=", self.st2,"age of st1=", self.st3,"age of st1=", self.st4)

class Department(studentdetails):
    def department(self):
        self.st1='IT'
        self.st2='Civil'
        self.st3='MEchanical'
        self.st4='Electrical'
        print("department of st1=",self.st1,"department of st2=", self.st2,"department of st3=", self.st3,"department of st4=", self.st4)
class totalmarks(Department):
    def languagetotalmarks(self):
        self.st1english="90"
        self.st2english="85"
        self.st3english="98"
        self.st4english="89"
        self.st1hindi="78"
        self.st2hindi="86"
        self.st3hindi="81"
        self.st4hindi="69"
        print("st1-english=", self.st1english,"st2-english=",self.st2english,"st3-english=",self.st3english,"st4-english=",self.st4english)
        print("st2-hindi=",self.st1hindi,"st2-hindi=",self.st2hindi,"st1-hindi=",self.st3hindi,"st1-english=",self.st4hindi)
        print("sum of st1's language marks is ",int(self.st1english)+int(self.st1hindi))
        print("sum of st2's language marks is ", int(self.st2english) + int(self.st2hindi))
ob=totalmarks()
ob.languagetotalmarks()
"""
"""class college:
    _name="pulkit"
    def fun1(self):
        print("in the school class")
class Teacher1(college):
    def fun2(self):
        print("in the Teacher1")

class Teacher2(college):
    def fun3(self):
        print("in the  TEacher2")

class student(Teacher1,Teacher2):
    def fun4(self):
        print("in the Student")
ob=student()
ob.fun1()
ob.fun2()
ob.fun3()
ob.fun4()
print(ob._name)"""
"""class exp:
    _name="pulkit"
class check(exp):
    pass
class check2(check):
    def __init__(self):
        print(self._name)
ob=check2()"""
"""class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
       # return "({0},{1})".format(self.x,self.y)
        return f"{self.x} {self.y}".format((self.x),(self.y))
p1=point("pulkit","tiwari")

print(p1)"""
"""class A:
    def __init__(self,a):
        self.a=a
    def __add__(self, o):
        return self.a+o.a
ob1=A(1)
ob2=A(2)
ob3=A("python")
ob4=A("for")
print(ob1+ob2)
print(ob3+ob4)
"""
"""class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self, o):
       if(self.a>o.a):
           return True
       else:
           return False
ob1=A(2)
ob2=A(3)
if (ob1>ob2):
    print("ob1 is greater tha ob2")
else :
    print("ob2 is greater than ob1")
"""
"""class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self, o):
       if(self.a<o.a):
           return True
       else:
           return False
    def __eq__(self, o):
        if (self.a == o.a):
            return True
        else:
            return False
ob1=A(2)
ob2=A(3)
ob3=A(5)
ob4=A(5)
if (ob1<ob2):
    print("ob1 is less tha ob2")
else :
    print("ob2 is less than ob1")

if (ob3 == ob4):
        print("ob1 and ob2 are equal")
else:
        print("ob1 and ob2 are not equal")"""

"""string="this is a python language"
a=(string.split())
for word in a:
    if len(word)%2== 0:
        print(word)"""
"""class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        c1=self.x+other.x
        c2=self.y+other.y
        return c1,c2


ob=C(13,4)
ob1=C(10,5)
print(ob1+ob)

"""
import random
print(random.randint(1,10))