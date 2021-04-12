#at first normal program
"""def name(func):
    func("hi this is unique")
name(print) """
#now see what is decorating
def dec():
    def nowexe():
        b= 5+6
        return nowexe
    print(nowexe())

dec()