class Employee:
    num=90
    def __init__(self,name1):
        self.name=name1


class Paradigm(Employee):
    pass
print(Paradigm.num)


pulkit=Employee("pulkit")
print(pulkit.name)
