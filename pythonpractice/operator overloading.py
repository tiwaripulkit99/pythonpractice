class employee:

    def __init__(self,m1,m2):
     self.m1=m1
     self.m2=m2

    def __add__(self, other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        return m1,m2
    def __repr__(self):
        return"hello both"
pulkit=employee(90,200)
vasim=employee(90,500)
print(pulkit)
print(vasim)
print(vasim+pulkit)
