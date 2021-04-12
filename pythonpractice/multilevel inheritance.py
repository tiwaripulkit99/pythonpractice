class dad:
   ball=8
   _protect

class son(dad):
    def __init__(self,name1):
        self.name=name1
class grandson(son):
    pass
pulkit=grandson("Pulkit")
print(pulkit.name)

