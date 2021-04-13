class kuchbhi:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def esehi(self):
        return (f"hello guys here is my name{self.fname}{self.lname}")
    @property
    def email(self):
        return f"{self.fname}{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
     name=string.split("@")[0]
     self.fname=name.split(".")[0]
     self.lname=name.split(".")[1]

pulkit=kuchbhi("pulkit","tiwari")
print(pulkit.fname)
print(pulkit.email)
pulkit.fname="yoyo"
print(pulkit.email)# but output will be the samen,not changing! so for it
pulkit.email="this.that @gmail.com"
print(pulkit.fname)
print(pulkit.email)