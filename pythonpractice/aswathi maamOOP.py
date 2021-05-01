"""class Exp:
    def normal(self,name):
        self.name=name

ob=Exp()
ob.normal("pulkit")
print(ob.name)"""
"""sum=0
for i in range(101):

    sum=sum+i
    print(f"the sum of numbers are ,sum)"""

"""
def even(n):
    i=1
    while n:
        yield 2*i
        i+=1
        n-=1
it=even(10)
print(next(it))
evenlist=[]
while True:
    try:
        evenlist.append(next(it))
    except StopIteration:
        break
print(evenlist)"""
"""list1 =[1,2,3,54]
list1.insert(2,9)
tuple1=(56,678,67,66)
print(list1)
list2=[10,23,90]
list1.append(tuple1)
list[5][2]=78
print(list1)"""
"""class check:
    @classmethod
    def ex(cls,*string):
        return cls (string.split("-"))
pulkit=check.ex("pulkit-hello-dude")
"""
"""def fun1():
    def fun2():
        a=3
        b=4
        print(a+b)
    return fun2
fun1()"""
"""class Student:
    stName="Pulkit tiwari"
    stClass="BCA"
    stId="00420"
    stGender="Male"
class child(Student):
    pass
ob1=child()
print(ob1.stId)
tuple=(1,)
print(tuple)
print(type(tuple))"""

"""class Student_Deatails:

    def __init__(self):
        self.name = 'somesh'
        self.age = 24
        self.gender = 'male'

class School(Student_Deatails):

    def __init__(self):
        Student_Deatails.__init__(self)
        self.school_name = "KRES"
        self.school_add = "Athani"

    def show(self):
        print('name :',self.name)
        print('age :', self.age)
        print('gender :', self.gender)
        print('school_name :', self.school_name)
        print('school_add :', self.school_add)
class Student_Sub(Student_Deatails):

    def __init__(self):
        Student_Deatails.__init__(self)
        self.stu_sub = 'php'
        self.marks = 54

    def show1(self):
        print('name :', self.name)
        print('age :', self.age)
        print('gender :', self.gender)
        print('stu_sub :', self.stu_sub)
        print('marks :', self.marks)

p = Student_Sub()
p.show1()
k = School()
k.show()"""
"""class base:
    def __init__(self):
        self.x=x
class derived(base):
    def __init__(self,x,y):
        base.x=x
        base.y=y
    def printxy(self):
        print()
d=derived(10,20)
d.printxy()"""

"""class Ex:
    countob = 0
    def __init__(self):
        print("hello")
        Ex.countob+=1
ob=Ex()
print(Ex.countob)"""
"""print("3",end="")
for i in range(5):
    print("r",end="")
for i in  range(5):
    print("i",end="")
"""
"""class employee1:
    def __init__(self):
        self.name="pulkit"
        self.age=21
class employee2:
    def __init__(self):
        self.name="yoyo"
        self.age=30
class employee(employee1,employee2):
    def __init__(self):
        self.name = "john"
        self.age = 35
em1=employee1()
em2=employee2()
print(em1.name)
"""
"""class number:
    def __init__(self):
        self.name = "yoyohoney"
class one(number):
    def __init__(self):
        self.name="yoyo"
class anything(one):
    def __init__(self):
        self.name="pulkit"
class anyinherit(anything):
    def __init__(self):

        self.name="tiwari"
        super().__init__()
        super(one, self).__init__()

ob=anyinherit()
print(ob.name)
"""
"""def add(x,y,z=0):
    return x+y+z
print(add(10,20))
print(add(10,20,30))
print(add())
"""
"""class india():
    def capital(self):
        print("new delhi is the capital of india")
    def language(self):
        print("hindi is most widely sopek languaeg in india")
    def type(self):
        print("india is developing country")
class USA():
    def capital(self):
        print("washington is the capital of india")
    def language(self):
        print("English is most widely sopek languaeg in india")
    def type(self):
        print("USA is developed country")
ob_india=india()
ob_USA=USA()
for country in (ob_india,ob_USA):
    country.capital()
    country.language()
    country.type()"""


"""class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):


    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):


        def flight(self):
            print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


"""
"""class Myclass:
    __hiddenvar=0
    def add(self,increment):
        self.__hiddenvar+=increment
        print(self.__hiddenvar)
myobject=Myclass()
myobject.add(2)
myobject.add(5)
print (myObject.__hiddenVariable)"""


"""class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 10


# Driver code
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)"""
"""class X():
    def __init__(self,a):
        self.num=a
    def doubleup(self):
        self.num*=2
class Y(X):
    def __init__(self,a):
        X.__init__(self,a)
    def tripleup(self):
        self.num*=3

obj = Y(4)
print(obj.num)

obj.doubleup()
print(obj.num)

obj.tripleup()
print(obj.num)"""

"""class Test:
    _name="pulkit"
class Mid(Test):
   pass
class check(Mid):
    def two(self):
        print(self._name)
ob=check()

ob.two()"""
"""list1=[1,2,3,4,4,55,55]
print(list1)
list1=set(list1)
print(list1)
print(list(list1))"""


# super class
"""class Super:
    # public data member
    var1 = None

    # protected data member
    _var2 = None

    # private data member
    __var3 = None

    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def displayPublicMembers(self):
        # accessing public data members
        print("Public Data Member: ", self.var1)

    # protected member function
    def _displayProtectedMembers(self):
        # accessing protected data members
        print("Protected Data Member: ", self._var2)

    # private member function
    def __displayPrivateMembers(self):
        # accessing private data members
        print("Private Data Member: ", self.__var3)

    # public member function
    def accessPrivateMembers(self):
        # accessing private memeber function
        self.__displayPrivateMembers()


# derived class
class Sub(Super):

    # constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

    # public member function
    def accessProtectedMemebers(self):
        # accessing protected member functions of super class
        self._displayProtectedMembers()


# creating objects of the derived class
obj = Sub("Tech", 4, "Tech !")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMemebers()
obj.accessPrivateMembers()

# Object can access protected member
print("Object is accessing protected member:", obj._var2)


# object can not access private member, so it will generate Attribute error
# print(obj.__var3)

"""
"""list=[56,78,675]
for index,item in enumerate(list):
    print(index,":",item)"""

while(True):
    if (5==6):
        print("hello")
    else:exit()



