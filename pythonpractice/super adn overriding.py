class A:
    clsvar=" I am the variable of cls A"
    def __init__(self):
        self.var1="I am instance variable of class A"
        self.clsvar="i am 2 nd instnce variable of class A "
        self.special="special"
class B(A):
    def __init__(self):

      self.var1="I am the variable of cls B"
      self.clsvar = "i am 2 nd instnce variable of class B"
      super().__init__()
      print(super().clsvar)#if we want to print clsvariable of class A

a=A()
b=B()
print(b.clsvar)