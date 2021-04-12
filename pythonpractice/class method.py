class student:
    marks=90
    @classmethod
    def nooofstu(cls,markz):
        cls.marks=markz

pulkit=student()
print(pulkit.marks)
pulkit.nooofstu(1000)
print(student.marks)
